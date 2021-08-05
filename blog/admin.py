from django.contrib import admin
from .models import Topic, Post

# Register your models here.

class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'excerpt',
        'publish',
        'author',
        'content',
        'topic',
        'status',
    )

    prepopulated_fields = {'slug':('title',)}
    ordering = ('author','topic',)

admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
