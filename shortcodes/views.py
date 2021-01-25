from django.shortcuts import render
from .models import ShortCode

# Create your views here.


def browse(request):
    codes = ShortCode.objects.all()
    context = {'codes': codes}
    template = 'shortcodes/browse.html'
    return render(request, template, context)
