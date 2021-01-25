from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from common.models import DateModel, Guest, Social, OpeningTime
from address.models import AddressField
from simple_search import search_filter
from django_resized import ResizedImageField


class Service(models.Model):
    name = models.CharField(max_length=80)
    icon = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class BusinessManager(models.Manager):
    def get_queryset(self):
        return super(BusinessManager, self).get_queryset().filter(active=True)

    def get_specific_business(self, name, state):
        query = name
        search_fields = ["name"]
        f = search_filter(search_fields, query)
        qs = self.get_queryset().filter(f)
        result = qs.filter(
            address__locality__state__name__icontains=state,
        )
        return result

    def top_rated_club(self, state):
        # top rated clubs
        return self.get_queryset().filter(
            address__locality__state__name__icontains=state, type="club", rating__gte=4
        )

    def six_closest_clubs(self, state):
        return (
            self.get_queryset()
            .filter(
                address__locality__state__name__icontains=state,
                type="club",
                featured=True,
            )
            .order_by("date_last_modified")[:6]
        )

    def closest_clubs(self, state):
        return (
            self.get_queryset()
            .filter(
                address__locality__state__name__icontains=state,
                type="club",
            )
            .order_by("date_last_modified")
        )

    def currently_hot_clubs(self, state):
        # currently hot clubs
        return self.get_queryset().filter(
            address__locality__state__name__icontains=state,
            type="club",
            currently_hot=True,
            featured=True,
        )


class Business(DateModel):
    category = [
        ("club", "Club"),
        ("organization", "Organization"),
        ("other", "Other"),
    ]
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(
        max_length=255,
        help_text="Unique value for product page URL, created from name.",
        unique=True,
    )
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
    featured = models.BooleanField(default=False)
    openning_times = models.ManyToManyField(OpeningTime)
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

    def get_phone_number(self):
        return "{}-{}".format(
            self.phone_number.country_code, self.phone_number.national_number
        )

    def get_address(self):
        return self.address.raw

    def get_absolute_url(self):
        return reverse("business:club_detail", args=[str(self.slug)])

    def get_thumbnail(self):
        business_image = self.images.all().filter(img_category="thumbnail")
        if business_image:
            thumbnail = business_image[0].image.url
            return thumbnail

    def get_gallery(self):
        business_image = self.images.all().filter(img_category="other")
        return business_image

    def get_social(self):
        return self.social.all()

    def get_slideshow(self):
        business_image = self.images.all().filter(img_category="slideshow")
        return business_image

    def get_latitude(self):
        return self.address.as_dict()["latitude"]

    def get_longitude(self):
        return self.address.as_dict()["longitude"]

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


class BusinessImage(DateModel):
    category = [
        ("thumbnail", "thumbnail"),
        ("other", "other"),
        ("top_slideshow", "slideshow"),
    ]
    business = models.ForeignKey(
        Business, related_name="images", on_delete=models.CASCADE
    )
    image = ResizedImageField(size=[480, 350], quality=75)
    img_category = models.CharField(max_length=20, choices=category, default="other")

    def __str__(self):
        return "{} {}".format(self.business.name, self.img_category)

    class Meta:
        db_table = "business_images"


class BusinessSocial(models.Model):
    business = models.ForeignKey(
        Business, related_name="social", on_delete=models.CASCADE
    )
    social = models.ForeignKey(Social, on_delete=models.CASCADE)
    url = models.URLField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.business.name, self.social.name)
