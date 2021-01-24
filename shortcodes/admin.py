from django.contrib import admin
from .models import ShortCode, ShortCodeLease


class ShortCodeAdmin(admin.ModelAdmin):
    list_display = (
        'shortcode',
        'description',
        'created_at',
        'is_available',
        'available_on',
    )


class ShortCodeLeaseAdmin(admin.ModelAdmin):
    list_display = (
        'leased_to',
        'shortcode',
        'description',
        'created_at',
        'expires_at',
        'is_active',
    )


# Register your models here.
admin.site.register(ShortCode, ShortCodeAdmin)
admin.site.register(ShortCodeLease, ShortCodeLeaseAdmin)
