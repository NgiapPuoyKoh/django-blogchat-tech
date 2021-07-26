import os
from django_blogchat_tech.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_protect
# from .models import Donation
import datetime
import stripe

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY') 


# Create your views here.
def donate(request):
    """ A view to return the donate page """
    return render(request, "donate/donate.html")


@csrf_protect
def charge(request):
    """ A view to process donation """

    if request.method == "POST":
        
        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email=request.POST['email'],
	        name=request.POST['username'],
	        source=request.POST['stripeToken']
		)

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='usd',
            description = 'Donation'
        )

        # donation.objects.create(
        #     donor = request.POST['username'],
        #     donate_date = datetime.date.today(),
        #     amount = amount,
        #     donated = True
        # )
       
    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
    """A view to notify donation successful """
    amount = args
    return render(request, 'donate/success.html', {'amount':amount})


# def donations(request):
#     """ A view to list donations """
#     # Consider restricting by user
#     donations = Donation.objects.all()

#     context = {
#         'donations' : donations
#     }

#     return render(request, 'donate/donations.html', context)


