from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("club",)


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
        return obj.venue.address.location

    def get_country(self, obj):
        return obj.venue.address.country

    def get_event(self, obj):
        return obj.event.name

    get_address.short_description = "Address"
    get_country.short_description = "Country"
    get_event.short_description = "Event"

    search_fields = (
        "event__name",
        "location__country",
    )
