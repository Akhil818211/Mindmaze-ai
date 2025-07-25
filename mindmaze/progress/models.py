from django.db import models
from django.conf import settings
from challenges.models import BrainGame
from datetime import date


class UserProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey('challenges.BrainGame', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    completed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.game.title} - {self.score}"


class DailyGoalTracker(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_streak = models.IntegerField(default=0)
    last_completed = models.DateField(null=True, blank=True)
    total_completed = models.IntegerField(default=0)

    def update_streak(self):
        today = date.today()
        if self.last_completed == today:
            return  # Already updated today
        elif self.last_completed == today.fromordinal(today.toordinal() - 1):
            self.current_streak += 1
        else:
            self.current_streak = 1  # Reset streak
        self.last_completed = today
        self.total_completed += 1
        self.save()

    @property
    def badge(self):
        if self.current_streak >= 30:
            return "Gold"
        elif self.current_streak >= 15:
            return "Silver"
        elif self.current_streak >= 5:
            return "Bronze"
        else:
            return "Newbie"

    def __str__(self):
        return f"{self.user.username} - Streak: {self.current_streak}"



class MindfulnessProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise = models.ForeignKey('mindfulness.MindfulnessExercise', on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.exercise.title}"
