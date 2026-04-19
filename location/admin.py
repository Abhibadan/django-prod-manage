from django.contrib import admin
from .models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "region", "city", "country", "zipcode", "address", "created_at")
    list_display_links = ("id",)
    search_fields = ("region", "city", "country", "zipcode", "address")
    ordering = ("country", "city", "-created_at")
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("region", "country")
    list_per_page = 10
    list_max_show_all = 20
    fieldsets = (
        ("Location Info", {"fields": ("region", "city", "country", "zipcode", "address")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
