from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    """
    A user profile model for maintaining user profiles
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80,
                            null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name or ''
