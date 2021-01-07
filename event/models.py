from django.db import models
from django.contrib.auth.models import User
from common.models import MusicGenre, Guest, Venue
from business.models import Business
from address.models import AddressField
import datetime  # important if using timezones
from simple_search import search_filter


# Create your models here.
class EventManager(models.Manager):
    def get_queryset(self):
        return super(EventManager, self).get_queryset().filter(active=True)

    def upcoming_events(self, state):
        # includes special and non special events
        return (
            self.get_queryset()
            .filter(
                location__locality__state__name__icontains=state,
                to_be_held_on__date__gte=datetime.date.today(),
            )
            .order_by("to_be_held_on")
        )

    def get_specific_event(self, name, state):
        # includes special and non special events
        query = name
        search_fields = ["name"]
        f = search_filter(search_fields, query)
        qs = self.get_queryset().filter(f).order_by("to_be_held_on")
        result = qs.filter(
            location__locality__state__name__icontains=state,
            to_be_held_on__date__gte=datetime.date.today(),
        )
        return result

    def upcoming_special_events(self, state):
        # includes special events only
        return (
            self.get_queryset()
            .filter(
                location__locality__state__name__icontains=state,
                to_be_held_on__date__gte=datetime.date.today(),
                is_special=True,
            )
            .order_by("to_be_held_on")
        )


class Event(models.Model):
    name = models.CharField(max_length=200, db_index=True)
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
    business = models.ManyToManyField(Business, related_name="business")
    guest = models.ManyToManyField(Guest, related_name="guest", blank=True)

    objects = models.Manager()  # The default manager.
    event_manager = EventManager()  # The useroffer manager.

    def __str__(self):
        return "{} {}".format(self.name, self.genre)

    def as_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "location": self.location.raw,
            "to_be_held_on": self.to_be_held_on.strftime("%Y-%m-%d %H:%M:%S"),
            "num_of_tickets": self.num_of_tickets,
            "business": [obj.as_dict() for obj in self.business.all()],
        }


class EventUser(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    visitor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Event User"

    def __str__(self):
        return "{} {}".format(self.event.name, self.visitor.username)
