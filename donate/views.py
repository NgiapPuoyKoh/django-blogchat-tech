import os
from django.conf import settings
from django_blogchat_tech.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import Donation
from django.contrib.auth import authenticate

import datetime
import stripe

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
# stripe_public_key = os.environ.get('STRIPE_PUBLIC_KEY')


# Create your views here.
def donate(request):
    """ A view to return the donate page """
    return render(request, "donate/donate.html")


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': os.environ.get('STRIPE_PUBLIC_KEY')}
        return JsonResponse(stripe_config, safe=False)


@csrf_protect
def charge(request):
    """ A view to process donation """

    if request.method == "POST":
        amount = int(request.POST['amount'])

        donation = Donation.objects.create(
            donor_name=request.POST['username'],
            donor_email=request.POST['email'],
            donate_date=datetime.date.today(),
            amount=request.POST['amount'],
            donated=True
        )

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['username'],
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='usd',
            description='Donation'
        )
    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
    """A view to notify donation successful """
    amount = args
    return render(request, 'donate/success.html', {'amount': amount})


def cancelMsg(request):
    """A view to notify donation has been cancelled """
    return render(request, 'donate/cancel.html')


def donations(request):
    """ A view to list donations """
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    if not request.user.is_staff:
        return redirect(reverse('user_profile', kwargs={'user': request.user}))

    donations = Donation.objects.all()

    context = {
        'donations': donations
    }
    return render(request, 'donate/donations.html', context)
