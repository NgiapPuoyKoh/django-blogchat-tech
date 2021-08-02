from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post


# Create your tests here.
class TestViews(TestCase):

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
    

    def test_fail_blog_page(self):
        """ TDD Fail Render blog Page """
        post1 = Post.objects.get(id=1)
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 302)


    # /donate/charge/100 will redirect to  /donate/success/100/
    # /donate/charge/ will redirect to /donate/success/5/
    # html page amount will be updated to donated amount
    # back to donation page link
    # def test_charge(self):
    # """Test charge stripe """


    def test_blog_home_page(self):
        """ Test blog page renders blog.html """
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')


    
    def test_blog_posts_list(self):
        """Test blog posts list renders posts.html with amount"""
        response = self.client.get(f'/blog/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/posts.html')


    def test_blog_post_detail(self):
        """Test post detail renders post_detail.html """
        post1 = Post.objects.get(id=1)
        response = self.client.get(f'/blog/post1.slug/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')


