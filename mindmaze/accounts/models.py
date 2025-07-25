from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    full_name.short_description = 'Full Name'



from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)
    days_active = models.IntegerField(default=0)
    challenges_completed = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)
    success_rate = models.FloatField(default=0.0)
    total_attempts = models.IntegerField(default=0)
    total_correct = models.IntegerField(default=0)
    level = models.CharField(max_length=50, default='Beginner')
    points = models.IntegerField(default=0)
    rank = models.CharField(max_length=50, default='N/A')

    def __str__(self):
        return self.user.username
