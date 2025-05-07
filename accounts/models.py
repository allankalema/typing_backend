from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields here
    typing_speed_goal = models.IntegerField(default=40)  # Words per minute goal
    
    def __str__(self):
        return self.username