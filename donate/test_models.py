from django.test import TestCase
from .models import Donation


class TestModels(TestCase):

    def test_donated_defaults_to_true(self):
       donation = Donation.objects.create(donor='Tester') 
       self.assertTrue(donation.donated)
    