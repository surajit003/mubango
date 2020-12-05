from django.db import models
from common.models import MusicGenre, Guest, Address, Venue
from business.models import Business

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


class EventSetUp(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    guest = models.ManyToManyField(Guest, related_name="guest", blank=True)
    price = models.IntegerField()
    to_be_held = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.business.name, self.event.name)
