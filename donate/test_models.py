from django.db import models
from django.test import TestCase
from .models import Donation
import datetime

class TestModels(TestCase):

    def test_donated_defaults_to_true(self):
       donation = Donation.objects.create(donor_name='Tester', donate_date=datetime.date.today() ) 
       self.assertTrue(donation.donated)
