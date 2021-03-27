from django.contrib import admin
from . import models


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("business", "user", "experience")
    search_fields = ("user__username",)


@admin.register(models.BusinessServiceRating)
class BusinessServiceAdmin(admin.ModelAdmin):
    list_display = (
        "service",
        "rating",
        "business",
        "user",
    )
    readonly_fields = ("rating",)
