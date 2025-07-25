from django.contrib import admin
from .models import MindfulnessExercise, MindfulnessSession

@admin.register(MindfulnessExercise)
class MindfulnessExerciseAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')


@admin.register(MindfulnessSession)
class MindfulnessSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'exercise', 'completed_at')
    list_filter = ('completed_at',)
