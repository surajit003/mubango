from django.db import models
from address.models import AddressField
from django.utils.translation import ugettext_lazy as _


class MusicGenre(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Guest(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Social(models.Model):
    name = models.CharField(max_length=120)
    icon = models.CharField(max_length=120)

    def __str__(self):
        return "{} {}".format(self.name, self.icon)


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


WEEKDAYS = [
    (1, _("Monday")),
    (2, _("Tuesday")),
    (3, _("Wednesday")),
    (4, _("Thursday")),
    (5, _("Friday")),
    (6, _("Saturday")),
    (7, _("Sunday")),
]


class OpeningTime(models.Model):

    weekday = models.IntegerField(choices=WEEKDAYS, unique=True)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        verbose_name = "OpeningTime"

    def __str__(self):
        return "{}-{}".format(self.from_hour, self.to_hour)
