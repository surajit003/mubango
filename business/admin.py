from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.BusinessServiceRating)
class BusinessServiceAdmin(admin.ModelAdmin):
    list_display = (
        "service",
        "rating",
        "business",
    )
    search_fields = ("business__name",)


@admin.register(models.Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "active",
        "rating",
        "get_address",
    )
    search_fields = ("name",)

    def get_address(self, obj):
        return obj.address.raw

    get_address.short_description = "Address"


@admin.register(models.VisitorCount)
class VisitorCountAdmin(admin.ModelAdmin):
    list_display = ("business", "count")
    search_fields = ("business",)
