from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from common.models import Address, DateModel, Rating


class Club(DateModel):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone_number = PhoneNumberField()
    active = models.BooleanField(default=False)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    price_type = models.CharField(max_length=10, null=True, blank=True)  # e.g $$$ or $$
    rating = models.ForeignKey(Rating, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.name, self.active)

    class Meta:
        verbose_name_plural = "Clubs"


class VisitorCount(DateModel):
    """
    can be used to keep track of users visiting clubs for a specific date
    """

    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    visitor = models.ManyToManyField(User)
    count = models.IntegerField(default=0)

    def __str__(self):
        return "{} {}".format(self.club.name, self.count)


class Trending(DateModel):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    thumbs_up_count = models.IntegerField(default=0)

    def __str__(self):
        return "{} {}".format(self.club.name, self.thumbs_up_count)
