from django.shortcuts import render

# Create your views here.
def donate(request):
    """ A view to return the donate page """
    return render(request, "donate/donate.html")
