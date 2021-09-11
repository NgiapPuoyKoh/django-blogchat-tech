from profiles.models import UserProfile
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .models import UserProfile
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.


class Topic(models.Model):

    options = {
        ('django', 'Django'),
        ('bootstrap5', 'Bootstrap5'),
        ('javascript', 'JavaScript'),
        ('sql', 'SQL'),
        ('whitenoise', 'Whitenoise'),
        ('stripe', 'Stripe')
    }

    class Meta:
        verbose_name_plural = 'Topics'

    name = models.CharField(
        max_length=254, choices=options, default='No Topic')
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Post(models.Model):

    class Meta:
        verbose_name_plural = 'Posts'

    options = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }

    title = models.CharField(max_length=254)
    excerpt = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')
    topic = models.ForeignKey(
        'Topic', null=True, blank=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

# Code Source: Try Django 1.9 - 29 of 38 - SlugField


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)


class Comment(models.Model):

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ("publish",)

    def __str__(self):
        return f"Comment by {self.name}"
