from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def profile(sender, instance, created, **kwargs):
    if created:
        create_profile(instance)


def create_profile(instance):
    try:
        Profile.objects.get(user=instance)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=instance)
        if profile:
            profile.slug = profile.profile_id
            profile.save()
