from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
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

    class Meta:
        verbose_name_plural = "Trending"

    def __str__(self):
        return "{} {}".format(self.club.name, self.count)


class Trending(DateModel):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    thumbs_up_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Trending"

    def __str__(self):
        return "{} {}".format(self.club.name, self.thumbs_up_count)


class Guest(DateModel):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    country = CountryField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class MusicGenre(DateModel):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(MusicGenre, related_name="music")
    priority_level = models.IntegerField(
        default=0
    )  # anyone creating the event can set priority

    def __str__(self):
        return "{} {}".format(self.name, self.genre)


class ClubEvent(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    guest = models.ManyToManyField(Guest, related_name="guest", blank=True)
    price = models.IntegerField()
    to_be_held = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.club.name, self.event.name)


class IndependentEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    guest = models.ManyToManyField(Guest, related_name="guest", blank=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    price = models.IntegerField()
    to_be_held = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{} {} {}".format(
            self.event.name, self.address.location, self.address.country
        )
