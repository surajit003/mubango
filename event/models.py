from django.db import models
from common.models import MusicGenre, Guest, Address, Venue
from club.models import Club

# Create your models here.
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
    guest = models.ManyToManyField(Guest, related_name="independent_guest", blank=True)
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT)
    price = models.IntegerField()
    to_be_held = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{} {} {}".format(
            self.event.name, self.venue.name, self.venue.address.country
        )
