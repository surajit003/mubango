from django.contrib import admin
from . import models


@admin.register(models.Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "icon",
    )


@admin.register(models.Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
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


@admin.register(models.OpeningTime)
class OpeningTimeAdmin(admin.ModelAdmin):
    list_display = ("id",)
