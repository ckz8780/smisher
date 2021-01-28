from django.shortcuts import render
from .models import Campaign

# Create your views here.


def user_campaigns(request):
    campaigns = Campaign.objects.filter(created_by=request.user.customer)
    context = {'campaigns': campaigns}
    template = 'campaigns/user_campaigns.html'
    return render(request, template, context)
