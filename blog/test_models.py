from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
# from profiles.models import UserProfile
from .models import Post, Topic

from django.utils import timezone
import datetime

class TestModels(TestCase):

    @classmethod
    def setUp(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username='Author1', password='Author1Pass', email = 'Author1@email.com')
        topic = Topic.objects.create(name='django', friendly_name= 'Django')
        Post.objects.create(
            title = 'How to test model',
            slug = 'How-to-test-model',
            publish = timezone.now(),
            author = user,
            content = 'Setup test data using <model>.objects.create',
            status = 'Draft',
            topic = topic
        )
    

    def test_post_is_assigned_slug_on_create(self):
        post1 = Post.objects.get(id=1)
        self.assertEquals(post1.slug, 'How-to-test-model')


    def test_status_defaults_to_draft(self):
        post1 = Post.objects.get(id=1)
        self.assertEquals(post1.status, 'Draft')


    def test_title_label(self):
        post1 = Post.objects.get(id=1)
        field_label = post1._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')


    def test_title_max_length(self):
        post1 = Post.objects.get(id=1)
        max_length = post1._meta.get_field('title').max_length
        self.assertEqual(max_length, 254)
    
    
    # def test_get_absolute_url(self):
    #     post1 = Post.objects.get(id=1)
    #     # This will also fail if the urlconf is not defined.
    #     self.assertEqual(post1.get_absolute_url(), '/blog/How-to-test-model/')
