from django.test import TestCase
from .models import UserProfile, User

# Create your tests here.

class TestModels(TestCase):
    
    @classmethod
    def setup(cls):
        user = get_user_model().objects.create_user(
                username='testuser', email='testemail@example.com',
                password='secret')
        UserProfile.objects.create( name='testuser',email='testemail@example.com' )


    def test_name_label(self):
        # UserProfile = UserProfile.objects.get(id=1)
        field_label = UserProfile._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')


    def test_email_label(self):
        # UserProfile = UserProfile.objects.get(id=1)
        field_label = UserProfile._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_name_max_length(self):
        # UserProfile = UserProfile.objects.get(id=1)
        max_length = UserProfile._meta.get_field('name').max_length
        self.assertEqual(max_length, 80)

    def test_email_max_length(self):
        # UserProfile = UserProfile.objects.get(id=1)
        max_length = UserProfile._meta.get_field('email').max_length
        self.assertEqual(max_length, 70)

