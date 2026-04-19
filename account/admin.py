from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','date_of_birth','phone_number')
    list_display_links = ('username',)
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    list_per_page = 10
    list_max_show_all = 20
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('phone_number', 'bio', 'address', 'avatar', 'date_of_birth')
        }),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {
            'fields': ('phone_number', 'bio', 'address', 'avatar', 'date_of_birth')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)