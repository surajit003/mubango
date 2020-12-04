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


@admin.register(models.ClubEvent)
class ClubEventAdmin(admin.ModelAdmin):
    list_display = (
        "get_event",
        "get_club",
    )
    search_fields = ("event__name",)

    def get_event(self, obj):
        return obj.event.name

    def get_club(self, obj):
        return obj.club.name

    get_event.short_description = "Event"
    get_club.short_description = "Club"


@admin.register(models.IndependentEvent)
class IndependentEventAdmin(admin.ModelAdmin):
    list_display = (
        "get_event",
        "get_address",
        "get_country",
    )

    def get_address(self, obj):
        return obj.address.location

    def get_country(self, obj):
        return obj.address.country

    def get_event(self, obj):
        return obj.event.name

    get_address.short_description = "Address"
    get_country.short_description = "Country"
    get_event.short_description = "Event"

    search_fields = (
        "event__name",
        "location__country",
    )
