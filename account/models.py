from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Country(models.Model):
    country = CountryField()


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=50, db_index=True, unique=True)

    class Meta:
        unique_together = ("country", "name")


class City(models.Model):
    state = models.ForeignKey(Country, on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=50, db_index=True, unique=True)

    class Meta:
        unique_together = ("state", "name")


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_id = models.CharField(max_length=120, unique=True, db_index=True)
    birth_date = models.DateField(null=True, blank=True)
