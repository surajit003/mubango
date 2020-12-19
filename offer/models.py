from django.db import models
from business.models import Business
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

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

    def update_offer_limit(sender, instance, **kwargs):
        if instance.offer.limit == 0:
            raise Exception("Cant redeem offer")
        else:
            instance.offer.limit = instance.offer.limit - 1
            instance.offer.save()


pre_save.connect(
    UserOffer.update_offer_limit, UserOffer, dispatch_uid="offer.useroffer"
)
