from django.shortcuts import render
from .models import LeaseListing

# Create your views here.


def listings(request):
    listings = LeaseListing.objects.all()
    context = {'listings': listings}
    template = 'marketplace/listings.html'
    return render(request, template, context)
