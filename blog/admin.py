from django.contrib import admin
from .models import Topic, Post, Comment

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
        'slug',
    )

    prepopulated_fields = {'slug': ('title',)}
    ordering = ('author', 'topic',)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'name',
        'email',
        'content',
        'publish',
        'status'
    )
    list_filter = (
        "status",
        "publish"
    )
    search_fields = (
        'name',
        'email',
        'content',
    )

    ordering = ('post', 'publish',)

admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
