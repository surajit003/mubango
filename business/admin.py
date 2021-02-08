from django.contrib import admin
from . import models

# Register your models here.
class ProductImagesInline(admin.StackedInline):
    model = models.BusinessImage


class SocialLink(admin.StackedInline):
    model = models.BusinessSocial


class BusinessServiceLink(admin.StackedInline):
    model = models.BusinessServiceRating


# @admin.register(models.Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ("name",)


# @admin.register(models.BusinessServiceRating)
# class BusinessServiceAdmin(admin.ModelAdmin):
#     list_display = (
#         "service",
#         "rating",
#         "business",
#     )
#     search_fields = ("business__name",)


@admin.register(models.Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "active",
        "rating",
        "get_address",
        "featured",
        "currently_hot",
    )
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImagesInline, SocialLink, BusinessServiceLink]

    def get_address(self, obj):
        return obj.address.raw

    get_address.short_description = "Address"


#
# @admin.register(models.VisitorCount)
# class VisitorCountAdmin(admin.ModelAdmin):
#     list_display = ("business", "count")
#     search_fields = ("business",)
#
#
# @admin.register(models.BusinessSocial)
# class BusinessSocialAdmin(admin.ModelAdmin):
#     list_display = ("business", "social", "url", "active")
