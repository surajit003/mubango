from django.contrib import admin
from . import models


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
        "state",
        "city",
        "get_country",
    )

    def get_country(self, obj):
        return obj.state.country.name

    get_country.short_description = "Country"


@admin.register(models.Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "country",
    )
    search_fields = ("first_name",)


@admin.register(models.MusicGenre)
class MusicGenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(models.Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )
    search_fields = ("name",)


@admin.register(models.Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "symbol",
    )
    search_fields = ("name",)
