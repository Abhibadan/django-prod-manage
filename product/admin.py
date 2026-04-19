from django.contrib import admin
from .models import Product, Order, avaialbility_log


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "is_active", "created_at", "added_by")
    list_display_links = ("name",)  # only name is underlined and opens the edit form
    list_filter = ("is_active", "added_by__username")
    search_fields = ("name", "description", "added_by__username")
    ordering = ("-created_at", "price", "name")
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 10
    list_max_show_all = 20
    fieldsets = (
        ("Product Info", {"fields": ("name", "description", "price", "is_active", "added_by")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "quantity", "ordered_by", "created_at")
    list_display_links = ("product",)  # only product is underlined and opens the edit form
    search_fields = ("product__name", "ordered_by__username")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 10
    list_max_show_all = 20
    fieldsets = (
        ("Order Info", {"fields": ("product", "quantity")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )


@admin.register(avaialbility_log)
class AvailabilityLogAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "location", "quantity", "created_at")
    list_display_links = ("product",)
    list_filter = ("location",)
    search_fields = ("product__name", "location__city", "location__region", "location__country", "location__zipcode",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 10
    list_max_show_all = 20
    fieldsets = (
        ("Availability Info", {"fields": ("product", "location", "quantity")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

