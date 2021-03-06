from django.db.models.signals import pre_save
from django.db.models import F
from django.dispatch import receiver
from .models import UserOffer


@receiver(pre_save, sender=UserOffer)
def update_offer_limit(sender, instance, **kwargs):
    validate_and_update_offer_limit(instance)


def validate_and_update_offer_limit(instance):
    if instance.offer.limit == 0:
        raise Exception("Cant redeem offer")
    else:
        instance.offer.limit = F("limit") - 1
        instance.offer.save()
