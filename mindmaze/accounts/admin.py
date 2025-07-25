from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _
from django.forms import TextInput, Textarea

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'full_name', 'is_staff', 'is_active']  # remove daily_goal
    list_filter = ['is_staff', 'is_superuser', 'is_active']

    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'password')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    search_fields = ['email', 'full_name']
    ordering = ['email']  # remove 'username'

admin.site.register(CustomUser, CustomUserAdmin)
