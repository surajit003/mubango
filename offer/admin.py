from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "code",
        "is_active",
        "is_special",
    )
    search_fields = (
        "title",
        "code",
        "business",
    )
