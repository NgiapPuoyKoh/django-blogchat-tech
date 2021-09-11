from django.contrib import admin
from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    """ User Profile admin """
    list_display = (
        'user',
        'name',
        'email',
    )


admin.site.register(UserProfile, UserProfileAdmin)
