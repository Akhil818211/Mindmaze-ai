from django.contrib import admin
from .models import UserProgress, DailyGoalTracker

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'completed_on')
    list_filter = ('completed_on',)

@admin.register(DailyGoalTracker)
class DailyGoalTrackerAdmin(admin.ModelAdmin):
    list_display = ('user', 'current_streak', 'total_completed', 'last_completed', 'badge')
