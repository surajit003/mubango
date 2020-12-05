from django.contrib import admin
from . import models

# Register your models here.


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
        return obj.address.location

    get_address.short_description = "Address"


@admin.register(models.VisitorCount)
class VisitorCountAdmin(admin.ModelAdmin):
    list_display = ("business", "count")
    search_fields = ("business",)


@admin.register(models.Trending)
class TrendingAdmin(admin.ModelAdmin):
    list_display = ("business", "thumbs_up_count")
    search_fields = ("business",)
