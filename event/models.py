from django.db import models
from django.contrib.auth.models import User
from common.models import MusicGenre, Guest, Venue
from business.models import Business
from address.models import AddressField

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(MusicGenre, related_name="music", blank=True)
    priority_level = models.IntegerField(
        default=0
    )  # anyone creating the event can set priority
    location = AddressField()
    to_be_held_on = models.DateTimeField()
    active = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)
    num_of_tickets = models.IntegerField(default=0)

    def __str__(self):
        return "{} {}".format(self.name, self.genre)


class EventOrganizer(models.Model):
    business = models.ManyToManyField(Business, related_name="business")
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    guest = models.ManyToManyField(Guest, related_name="guest", blank=True)

    class Meta:
        verbose_name_plural = "Event SetUp"

    def __str__(self):
        return "{} {}".format(self.business.name, self.event.name)


class EventUser(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    visitor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Event User"

    def __str__(self):
        return "{} {}".format(self.event.name, self.visitor.username)
