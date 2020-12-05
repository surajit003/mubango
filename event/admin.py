from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("business",)


@admin.register(models.EventSetUp)
class EventSetUpAdmin(admin.ModelAdmin):
    list_display = (
        "get_event",
        "get_business",
    )
    search_fields = ("event__name",)

    def get_event(self, obj):
        return obj.event.name

    def get_business(self, obj):
        return obj.business.name

    get_event.short_description = "Event"
    get_business.short_description = "Business"
