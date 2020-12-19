from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import UserOffer


@receiver(pre_save, sender=UserOffer)
def update_offer_limit(sender, instance, **kwargs):
    if instance.offer.limit == 0:
        raise Exception("Cant redeem offer")
    else:
        instance.offer.limit = instance.offer.limit - 1
        instance.offer.save()
