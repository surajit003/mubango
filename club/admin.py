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
