from django.db.models.signals import pre_save
from django.db.models import F
from django.dispatch import receiver
from .models import EventUser


@receiver(pre_save, sender=EventUser)
def update_offer_limit(sender, instance, **kwargs):
    validate_and_update_ticket(instance)


def validate_and_update_ticket(instance):
    if instance.event.num_of_tickets == 0:
        raise Exception("No more tickets left for this event")
    else:
        instance.event.num_of_tickets = F("num_of_tickets") - 1
        instance.event.save()
