from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class TestViews(TestCase):

    def test_donate_page(self):
        """ Test donate page renders donate.html """
        response = self.client.get('/donate/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donate/donate.html')

    def test_successMsg(self):
        """Test donate success renders success.html with amount"""
        amount = 10
        response = self.client.get(f'/donate/success/{amount}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donate/success.html')

    def test_cancelMsg(self):
        """Test donate cancel renders cancel.html """
        response = self.client.get(f'/donate/cancel/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donate/cancel.html')

    def test_donation_page(self):
        """ Test donation page renders donations.html """
        response = self.client.get('/donate/donations')
        self.assertEqual(response.status_code, 301)

