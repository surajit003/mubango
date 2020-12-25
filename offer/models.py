from django.db import models
from business.models import Business
from django.contrib.auth.models import User
from .utils import calculate_distance
from address.models import AddressField

# Create your models here.
class OfferManager(models.Manager):
    def get_queryset(self):
        return super(OfferManager, self).get_queryset().filter(active=True)

    def top_five_offer_based_on_user_state(self, state):
        return self.get_queryset().filter(
            location__locality__state__name__icontains=state
        )

    def top_five_closest_offer_based_on_user_geolocation(self, state, coordinates):
        qs = self.top_five_offer_based_on_user_state(state)
        distance_user_offer = {}
        if qs.exists():
            for q in qs:
                offer_location_coordinate = [
                    q.location.latitude,
                    q.location.longitude,
                ]
                distance_user_offer[q.id] = calculate_distance(
                    coordinates, offer_location_coordinate
                )
            distance_user_offer = dict(
                sorted(
                    distance_user_offer.items(),
                    key=lambda distance_user_offer: distance_user_offer[1],
                )
            )
        return list(distance_user_offer.items())[:5]


class Offer(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    location = AddressField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)
    code = models.CharField(max_length=120, blank=True, null=True)
    limit = models.IntegerField(default=0)

    objects = models.Manager()  # The default manager.
    user_offer = OfferManager()  # The useroffer manager.

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        unique_together = ("business", "title")
        verbose_name_plural = "Offers"


class UserOffer(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.offer.title

    class Meta:
        verbose_name_plural = "UserOffer"
        unique_together = ("user", "offer")
