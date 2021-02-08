from django.contrib import admin
from . import models
from .forms import OfferForm

# Register your models here.


class OfferImageInline(admin.StackedInline):
    model = models.OfferImage


class OfferSocialInline(admin.StackedInline):
    model = models.OfferSocial


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
    prepopulated_fields = {"slug": ("title",)}
    search_fields = (
        "title",
        "code",
        "business",
    )
    inlines = [OfferImageInline, OfferSocialInline]

    def get_business_name(self, obj):
        return obj.business.name

    get_business_name.short_description = "Business"
