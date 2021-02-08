from django.contrib import admin
from . import models

# Register your models here.
class EventImagesInline(admin.StackedInline):
    model = models.EventImage


class EventServiceInline(admin.StackedInline):
    model = models.EventServiceRating


class EventSocialInline(admin.StackedInline):
    model = models.EventSocial


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "active",
        "featured",
    )
    search_fields = ("business",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [EventImagesInline, EventServiceInline, EventSocialInline]
