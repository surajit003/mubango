from django.contrib import admin
from . import models
from .forms import OfferForm

# Register your models here.


@admin.register(models.Offer)
class OfferAdmin(admin.ModelAdmin):
    form = OfferForm
    list_display = (
        "id",
        "title",
        "code",
        "active",
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


@admin.register(models.UserOffer)
class UserOffer(admin.ModelAdmin):
    list_display = (
        "id",
        "offer",
        "user",
    )
