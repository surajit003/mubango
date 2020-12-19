from django.db import models
from business.models import Business
from django.contrib.auth.models import User

# Create your models here.


class Offer(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)
    code = models.CharField(max_length=120, blank=True, null=True)
    limit = models.IntegerField(default=0)

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
