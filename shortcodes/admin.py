from django.contrib import admin
from .models import ShortCode, ShortCodeLease

# Register your models here.
admin.site.register(ShortCode)
admin.site.register(ShortCodeLease)