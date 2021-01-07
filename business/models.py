from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from common.models import DateModel, Guest
from address.models import AddressField


class Service(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class BusinessManager(models.Manager):
    def get_queryset(self):
        return super(BusinessManager, self).get_queryset().filter(active=True)

    def top_rated_club(self, state):
        # top rated clubs
        return self.get_queryset().filter(
            address__locality__state__name__icontains=state, type="club", rating__gte=4
        )

    def closest_clubs(self, state):
        # closest clubs
        return self.get_queryset().filter(
            address__locality__state__name__icontains=state,
            type="club",
        )

    def currently_hot_clubs(self, state):
        # currently hot clubs
        return self.get_queryset().filter(
            address__locality__state__name__icontains=state,
            type="club",
            currently_hot=True,
        )


class Business(DateModel):
    category = [
        ("club", "Club"),
        ("organization", "Organization"),
        ("other", "Other"),
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone_number = PhoneNumberField()
    active = models.BooleanField(default=False)
    type = models.CharField(max_length=30, choices=category, default="other")
    address = AddressField()
    price_type = models.CharField(max_length=10, null=True, blank=True)  # e.g $$$ or $$
    rating = models.IntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    currently_hot = models.BooleanField(default=False)
    objects = models.Manager()  # The default manager.
    business_manager = BusinessManager()  # The useroffer manager.

    def __str__(self):
        return "{} {}".format(self.name, self.active)

    def as_dict(self):
        return {
            "name": self.name,
            "location": self.address.raw,
            "rating": self.rating,
            "price_type": self.price_type,
            "phone_number": "{}-{}".format(
                self.phone_number.country_code, self.phone_number.national_number
            ),
        }

    class Meta:
        verbose_name_plural = "Businesses"


class BusinessServiceRating(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{} {} {}".format(self.service.name, self.business.name, self.rating)


class VisitorCount(models.Model):
    """
    can be used to keep track of users visiting business e.g club for a specific date
    """

    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    visitor = models.ManyToManyField(User)
    count = models.IntegerField(default=0)
    date_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "VisitorCount"

    def __str__(self):
        return "{} {}".format(self.business.name, self.count)
