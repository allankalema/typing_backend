from django.db import models
from accounts.models import CustomUser

class TextPassage(models.Model):
    content = models.TextField()
    difficulty = models.CharField(max_length=20, choices=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.difficulty} passage ({self.id})"

class TypingSession(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    passage = models.ForeignKey(TextPassage, on_delete=models.CASCADE)
    wpm = models.FloatField()
    accuracy = models.FloatField()
    errors = models.JSONField()  # Stores words with errors and their counts
    time_taken = models.FloatField()  # In seconds
    date_completed = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username if self.user else 'Anonymous'} - {self.wpm} WPM"