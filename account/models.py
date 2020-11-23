from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Country(models.Model):
    country = CountryField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_id = models.CharField(max_length=120,unique=True,db_index=True)
    birth_date = models.DateField(null=True, blank=True)



