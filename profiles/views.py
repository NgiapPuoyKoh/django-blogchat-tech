from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import EditProfileForm
from django.contrib.auth.models import User

# Create your views here.

@login_required
def user_profile(request, user):
    """ A view to return the profile page """

    if not request.user.is_authenticated:
        return redirect(reverse('home'))

    context = {
        'user': user,
    }

    try:
        get_user = get_object_or_404(User, username=user)

        user_profile = get_object_or_404(UserProfile, user=get_user)

        context = {
                'user_profile': user_profile,
                'user': get_user,
            }

        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        return render(request, 'profiles/profile.html', context)


@login_required
def edit_profile(request, user):
    """ A function to edit the users profile and render
    the edit_profile page """

    # try:
    #     profile = get_object_or_404(UserProfile, user=request.user)

    # except Exception as e:
    #     # Create empty User Profile if it doesn't exist
    #     UserProfile.objects.create(
    #         user=request.user, 
    #         name='',
    #         email='')

    get_user = get_object_or_404(User, username=user)
    profile = get_object_or_404(UserProfile, user=get_user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if "cancel" in request.POST:
            return redirect(reverse('user_profile', args=[user]))
        elif form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
            return redirect(reverse('user_profile', args=[user]))
        else:
            messages.error(request,
                           'Profile update failed.'
                           'Please ensure the form is valid!')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profiles/edit_profile.html', context)


@login_required
def delete_profile(request, user):
    """ Delete current logged in user"""

    if not request.user.is_authenticated:
        return render(request, 'home/index.html')

    if request.user.username == user:
        user = request.user
        user.delete()

    return redirect(reverse('home'))
