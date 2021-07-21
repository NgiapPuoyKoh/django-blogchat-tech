from django.test import TestCase, Client
from django.urls import reverse
from .models import UserProfile
from django.contrib.auth.models import User

# Create your tests here.
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username = 'Tester', password='testerpass')

    def test_get_profile_page(self):
        """ Test profile page renders for user """
        login = self.client.login(username='Tester', password='testerpass')
        response = self.client.get(reverse('user_profile', kwargs = {'user': self.user}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_get_edit_profile_page(self):
        """ Test edit profile page renders for user """
        login = self.client.login(username='Tester', password='testerpass')
        response = self.client.get(reverse('edit_profile', kwargs = {'user': self.user}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/edit_profile.html')

    def test_profile_page_redirect_when_logged_out(self):
        """ Test profile page redirects to home when logged out """
        response = self.client.get('/profiles/user/')
        self.assertEqual(response.status_code, 302)

    def test_edit_profile_post(self):
        """ Test edit profile POST"""
        login = self.client.login(username='Tester', password='testerpass')
        response = self.client.post(reverse('edit_profile', kwargs = {'user': self.user}), {'user': self.user,  'name':'Name Updated', 'email': 'updatedemail@test.com'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user_profile', kwargs = {'user': self.user}))

    def test_edit_profile_get(self):
        """ Test edit profile POST"""
        login = self.client.login(username='Tester', password='testerpass')
        response = self.client.get(reverse('edit_profile', kwargs = {'user': self.user}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/edit_profile.html')

    def test_delete_profile(self):
        """ Test delete profile """
        login = self.client.login(username='Tester', password='testerpass')
        response = self.client.delete(reverse('delete_profile', kwargs = {'user': self.user}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))


