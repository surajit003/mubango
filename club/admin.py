from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "active",
        "rating",
        "get_address",
    )
    search_fields = ("name",)

    def get_address(self, obj):
        return obj.address.location

    get_address.short_description = "Address"


@admin.register(models.VisitorCount)
class VisitorCountAdmin(admin.ModelAdmin):
    list_display = ("club", "count")
    search_fields = ("club",)


@admin.register(models.Trending)
class VisitorCountAdmin(admin.ModelAdmin):
    list_display = ("club", "thumbs_up_count")
    search_fields = ("club",)


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "to_be_held",
        "price",
    )
    search_fields = ("club",)


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
