from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "active",
        "featured",
    )
    search_fields = ("business",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.EventUser)
class EventUserAdmin(admin.ModelAdmin):
    list_display = (
        "get_event",
        "get_user",
    )
    search_fields = ("event__name", "user__username")

    def get_event(self, obj):
        return obj.event.name

    def get_user(self, obj):
        return obj.visitor.username

    get_event.short_description = "Event"
