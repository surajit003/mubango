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
        "get_business_name",
    )
    search_fields = (
        "title",
        "code",
        "business",
    )

    def get_business_name(self, obj):
        return obj.business.name

    get_business_name.short_description = "Business"
