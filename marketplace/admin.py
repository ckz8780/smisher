from django.contrib import admin
from marketplace.models import LeaseListing, LeaseHistory, LeaseTransaction

# Register your models here.


class LeaseListingAdmin(admin.ModelAdmin):
    list_display = (
        'listing_id',
        'listed_by',
        'lease',
        'price',
        'description',
        'created_at',
        'expires_at',
        'is_active',
    )


class LeaseHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'lease',
        'original_lease'
    )


class LeaseTransactionAdmin(admin.ModelAdmin):
    list_display = (
        'lease_history',
        'transferred_from',
        'transferred_to',
        'original_from',
        'original_to',
        'txn_date',
        'txn_type',
        'txn_value',
        'notes',
    )


admin.site.register(LeaseListing, LeaseListingAdmin)
admin.site.register(LeaseHistory, LeaseHistoryAdmin)
admin.site.register(LeaseTransaction, LeaseTransactionAdmin)
