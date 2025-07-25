from django.contrib import admin
from .models import BrainGame

@admin.register(BrainGame)
class BrainGameAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty')
    search_fields = ('title',)
    list_filter = ('difficulty',)
