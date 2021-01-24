from django.contrib import admin
from .models import ShortCode, ShortCodeLease


class ShortCodeAdmin(admin.ModelAdmin):
    list_display = (
        'shortcode',
        'description',
        'created_at',
        'is_available',
        'get_lease',
        'available_on',
    )

    def get_lease(self, instance):
        if instance.lease:
            return instance.lease.leased_to.cust_name
        return None
    get_lease.short_description = 'Leased To'


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
