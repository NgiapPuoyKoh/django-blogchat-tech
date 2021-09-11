from profiles.models import UserProfile
from django.test import TestCase
from .forms import EditProfileForm

# Create your tests here.


class TestViews(TestCase):

    # def test_profile_fields_are_required(self):
    #     form = EditProfileForm({'name': 'Name'})
    #     self.assertTrue(form.is_valid())
    #     self.assertIn('name', form.errors.keys())
    #     self.assertEqual(form.errors['name'][0],'This field is required.')

    def test_profile_name_field_not_required(self):
        form = EditProfileForm({'name': 'Tester Name'})
        self.assertTrue(form.is_valid())

    def test_profile_email_field_not_required(self):
        form = EditProfileForm({'email': 'test@email.com'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = EditProfileForm()
        self.assertEqual(form.Meta.fields, ['name', 'email'])

# profile url and html if logged in else redirect to home

# Redirect to home on logout

# Form Required fields
