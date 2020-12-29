from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from common.models import DateModel
from address.models import AddressField
import datetime


class Profile(DateModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    verification_id = models.CharField(max_length=120, unique=True, db_index=True)
    birth_date = models.DateField(null=True, blank=True)
    points = models.IntegerField(default=0)
    phone_number = PhoneNumberField()
    active = models.BooleanField(default=False)
    address = AddressField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.user.username, self.active)

    class Meta:
        verbose_name_plural = "Profiles"

    def months_on_mubango(self):
        date_joined = self.user.date_joined.replace(tzinfo=None)
        now = datetime.datetime.now()
        relative_delta = abs(now - date_joined)
        if hasattr(relative_delta, "days"):
            remaining_days = relative_delta.days
            months = int(round(remaining_days / 30))
            if months < 1:
                return "{}:{}".format("days", remaining_days)
            else:
                return "{}:{}".format("months", months)


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower"
    )
    followed_date = models.DateField(auto_now=True)
    unfollowed_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.user, self.follower)

    class Meta:
        verbose_name_plural = "Followers"
