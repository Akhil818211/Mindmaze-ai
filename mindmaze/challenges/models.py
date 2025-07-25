from django.db import models
from django.conf import settings

class BrainGame(models.Model):
    CHALLENGE_TYPES = (
        ('spatial', 'Spatial'),
        ('code breaking', 'Code Breaking'),
        ('logic','Logic'),
        ('riddle','Riddle'),
        ('math','Math'),
        ('memory','Memory'),
    )

    DIFFICULTY_LEVELS = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
        
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    challenge_type = models.CharField(max_length=20, choices=CHALLENGE_TYPES)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVELS, default='easy')  # ✅ Added
    question = models.TextField()
    correct_answer = models.CharField(max_length=100)

    def __str__(self):
        return self.title
