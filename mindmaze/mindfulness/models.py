from django.db import models
from django.conf import settings

class MindfulnessExercise(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField(help_text="Breathing script, instructions, or calm activity")

    def __str__(self):
        return self.title


class MindfulnessSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise = models.ForeignKey(MindfulnessExercise, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.exercise.title} - {self.user.username} - {self.completed_at.date()}"
