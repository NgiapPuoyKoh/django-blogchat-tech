from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from profiles.models import UserProfile

# Create your models here.


class Donation(models.Model):
    """
    A model to record donations
    """
    donor_name = models.CharField(max_length=50)
    donor_email = models.EmailField(max_length=254)
    donate_date = models.DateTimeField(
        max_length=80, null=False, blank=False)
    amount = models.IntegerField(default=0)
    donated = models.BooleanField(default=True)

    def __str__(self):
        return self.donor_name
