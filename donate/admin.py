from django.contrib import admin
from .models import Donation, UserProfile

# Register your models here.

class UserDonationAdmin(admin.ModelAdmin):
    """ User Donation Admin """
    list_display = (
        # 'donor_username',
        'donor_name',
        'donor_email',
        'donate_date',
        'amount',
        'donated',
    )

admin.site.register(Donation, UserDonationAdmin)

# from .models import UserProfile
# Register your models here.

# class UserProfileAdmin(admin.ModelAdmin):
#     """ User Profile admin """
#     list_display = (
#         'user',
#         'name',
#         'email',
#     )

# admin.site.register(UserProfile, UserProfileAdmin)