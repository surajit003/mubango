from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from common.models import Address, DateModel, Rating, Guest


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
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    price_type = models.CharField(max_length=10, null=True, blank=True)  # e.g $$$ or $$
    rating = models.ForeignKey(Rating, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.name, self.active)

    class Meta:
        verbose_name_plural = "Clubs"


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


class Trending(DateModel):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    thumbs_up_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Trending"

    def __str__(self):
        return "{} {}".format(self.business.name, self.thumbs_up_count)
