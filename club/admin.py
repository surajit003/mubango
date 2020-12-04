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
    list_display = ("club", "visitor", "count")
    search_fields = ("club",)
