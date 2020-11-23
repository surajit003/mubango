from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    list_display = ("name", "country")


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state")


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "location",
        "country",
        "state",
        "city",
    )


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "verification_id",
    )
