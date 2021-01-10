from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.urls import reverse
from common.models import MusicGenre, Guest, Venue, Social, DateModel
from business.models import Business, Service
from address.models import AddressField
import datetime  # important if using timezones
from simple_search import search_filter
from phonenumber_field.modelfields import PhoneNumberField


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
    slug = models.SlugField(
        max_length=255,
        help_text="Unique value for product page URL, created from name.",
        unique=True,
    )
    description = models.TextField(null=True, blank=True)
    phone_number = PhoneNumberField()
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
    featured = models.BooleanField(default=False)
    old_price = models.DecimalField(default=1, decimal_places=2, max_digits=5)
    new_price = models.DecimalField(default=1, decimal_places=2, max_digits=5)

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

    def get_address(self):
        return self.location.raw

    def get_phone_number(self):
        return "{}-{}".format(
            self.phone_number.country_code, self.phone_number.national_number
        )

    def get_price(self):
        if self.new_price <= self.old_price:
            return self.new_price

    def get_latitude(self):
        return self.location.as_dict()["latitude"]

    def get_longitude(self):
        return self.location.as_dict()["longitude"]

    def get_thumbnail(self):
        event_image = EventImage.objects.get(event=self.id, img_category="thumbnail")
        thumbnail = event_image.image.url
        return thumbnail

    def get_date(self):
        return self.to_be_held_on.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse("event:event_detail", args=[str(self.slug)])


class EventUser(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    visitor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Event User"

    def __str__(self):
        return "{} {}".format(self.event.name, self.visitor.username)


class EventImage(DateModel):
    category = [
        ("thumbnail", "thumbnail"),
        ("other", "other"),
        ("top_slideshow", "slideshow"),
    ]
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = ResizedImageField(size=[480, 350], quality=75)
    img_category = models.CharField(max_length=20, choices=category, default="other")

    def __str__(self):
        return "{} {}".format(self.event.name, self.img_category)

    class Meta:
        db_table = "event_images"


class EventSocial(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    social = models.ForeignKey(Social, on_delete=models.CASCADE)
    url = models.URLField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.event.name, self.social.name)


class EventServiceRating(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{} {} {}".format(self.service.name, self.event.name, self.rating)
