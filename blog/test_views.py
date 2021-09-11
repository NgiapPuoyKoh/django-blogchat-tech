from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Topic
from django.utils import timezone
from django.utils.text import slugify
from blog.forms import PostSearchForm

# Create your tests here.


class TestViews(TestCase):

    @classmethod
    def setUp(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(
            username='Author1', password='Author1Pass',
            email='Author1@email.com')
        topic = Topic.objects.create(name='django', friendly_name='Django')
        post1 = Post.objects.create(
            title='How to test model',
            slug='Howtotestmodel',
            publish=timezone.now(),
            author=user,
            content='Setup test data using <model>.objects.create',
            status='Draft',
            topic=topic
        )

    def test_fail_blog_page(self):
        """ TDD Fail Render blog Page """
        post1 = Post.objects.get(id=1)
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_blog_home_page(self):
        """ Test blog page renders blog.html """
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_blog_posts_list(self):
        """Test blog posts list renders posts.html"""
        posts = Post.objects.all()
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/posts.html')

    def test_posts_search(self):
        """Test blog posts search renders posts.html"""
        response = self.client.get(reverse('posts_search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/search.html')

    # def test_posts_search_get(self):
    #     """Test blog posts search get renders posts.html"""
    #     response = self.client.get(reverse('posts_search'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/search.html')\

    # def test_blog_post_detail(self):
    #     """Test post detail renders post_detail.html """
    #     post1 = Post.objects.get(id=1)
    #     response = self.client.get(reverse('post_detail', post1.slug))
    # #     response = self.client.get(reverse('post_detail', post1.slug)
    # #     # response = self.client.get(f'{post1.slug}')
    # #     # response = self.client.get(reverse(f'{post1.slug}'))
    #     # response = self.client.get(reverse('post_detail', post1.slug))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/post_detail.html')
