from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
