from django.contrib import admin
from . import models

# Register your models here.
class ProductImagesInline(admin.StackedInline):
    model = models.BusinessImage


class SocialLink(admin.StackedInline):
    model = models.BusinessSocial


@admin.register(models.Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "active",
        "get_address",
        "featured",
        "currently_hot",
    )
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImagesInline, SocialLink]

    def get_address(self, obj):
        return obj.address.raw

    get_address.short_description = "Address"
