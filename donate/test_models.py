from django.db import models
from django.test import TestCase
from .models import Donation
from django.utils import timezone
import datetime


class TestModels(TestCase):

    def test_donated_defaults_to_true(self):
        donation = Donation.objects.create(
            donor_name='Tester', donate_date=timezone.now())
        self.assertTrue(donation.donated)
