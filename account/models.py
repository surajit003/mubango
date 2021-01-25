from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField
from common.models import DateModel
from address.models import Address
import datetime
import uuid


class Profile(DateModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_id = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    verification_id = models.CharField(max_length=120, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    points = models.IntegerField(default=0)
    phone_number = PhoneNumberField()
    active = models.BooleanField(default=False)
    address = models.ForeignKey(
        Address, null=True, blank=True, on_delete=models.CASCADE
    )
    image = ResizedImageField(size=[480, 350], quality=75, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.user.username, self.active)

    def get_address(self):
        if self.address:
            return self.address.raw

    def get_image(self):
        if self.image:
            return self.image.url

    class Meta:
        verbose_name_plural = "Profiles"

    def months_on_mubango(self):
        date_joined = self.user.date_joined.replace(tzinfo=None)
        now = datetime.datetime.now()
        relative_delta = abs(now - date_joined)
        if hasattr(relative_delta, "days"):
            remaining_days = int(relative_delta.days)
            months = int(round(remaining_days / 30))
            if months < 1:
                return "{}:{}".format("days", remaining_days)
            else:
                return "{}:{}".format("months", months)

    def get_state(self):
        if self.address:
            return self.address.locality.state.name
        else:
            return "Nairobi"

    def get_follower_count(self):
        return self.user.user.all().count()


class Follower(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", db_index=True
    )
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower"
    )
    followed_date = models.DateField(auto_now=True)
    unfollowed_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.user, self.follower)

    class Meta:
        verbose_name_plural = "Followers"
        unique_together = ("user", "follower")
