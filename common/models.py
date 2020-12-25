from django.db import models
from address.models import AddressField


class Rating(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10, unique=True)
    additional_description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Ratings"

    def __str__(self):
        return "{} {}".format(self.name, self.symbol)


class MusicGenre(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Guest(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Venue(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    address = AddressField()

    def __str__(self):
        return "{} {}".format(self.name, self.description)


class DateModel(models.Model):
    """
    An abstract base class model that provides self-
    . fields.
    updating ``created`` and ``modified``
    """

    date_last_modified = models.DateField(auto_now=True)
    date_added = models.DateField(auto_now=True)

    class Meta:
        abstract = True
