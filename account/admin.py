from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "phone_number",
    )
    prepopulated_fields = {"slug": ("profile_id",)}


@admin.register(models.Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "follower",
    )
