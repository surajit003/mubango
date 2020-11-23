from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class Country(models.Model):
    country = CountryField()

    def __str__(self):
        return self.country.name

    class Meta:
        verbose_name_plural = "countries"


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=50, db_index=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("country", "name")
        verbose_name_plural = "states"


class City(models.Model):
    state = models.ForeignKey(Country, on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=50, db_index=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("state", "name")
        verbose_name_plural = "cities"


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "addresses"

    def __str__(self):
        return self.location


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    verification_id = models.CharField(max_length=120, unique=True, db_index=True)
    birth_date = models.DateField(null=True, blank=True)
    points = models.IntegerField(default=0)
    phone_number = PhoneNumberField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.user.username, self.active)

    class Meta:
        verbose_name_plural = "profiles"
