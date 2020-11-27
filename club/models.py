from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from common.models import Address, DateModel


class Club(DateModel):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone_number = PhoneNumberField()
    active = models.BooleanField(default=False)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    price = models.CharField(
        max_length=10, null=True, blank=True
    )  # not actual price per se more like $$$ or $$

    def __str__(self):
        return "{} {}".format(self.name, self.active)

    class Meta:
        verbose_name_plural = "Clubs"
