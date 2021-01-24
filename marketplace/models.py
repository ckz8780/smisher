import uuid
from django.db import models
from customers.models import Customer
from shortcodes.models import ShortCode, ShortCodeLease
from smisher.utils import get_default_expiration


# Create your models here.
class LeaseListing(models.Model):

    class Meta:
        ordering = ('-created_at',)
        # Restrict to only one active listing at a time
        constraints = [models.UniqueConstraint(
            name="unique_active_lease_listing",
            fields=['lease'],
            condition=models.Q(is_active=True),
        )]
        # TODO: restrict creating listings to the current owner of the lease

    listing_id = models.UUIDField(default=uuid.uuid4, editable=False)
    listed_by = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='lease_listings')
    lease = models.ForeignKey(ShortCodeLease, on_delete=models.CASCADE, related_name='listing')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=300)
    lease_expires = models.DateTimeField(null=True, blank=True)  # TODO: This shouldn't be nullable; find a better way
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=get_default_expiration)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.lease_expires = self.lease.expires_at
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.listing_id)


class LeaseHistory(models.Model):

    class Meta:
        verbose_name_plural = 'Lease histories'

    # Field is required in admin, but can be null if leaseis deleted
    lease = models.ForeignKey(ShortCodeLease, on_delete=models.SET_NULL, null=True)
    # TODO: If linked lease is deleted, cache original ID here for reference
    original_lease = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        if self.lease:
            return f'History for {self.lease}'
        return f'History for {self.original_lease}'


class LeaseTransaction(models.Model):

    class Meta:
        ordering = ('-txn_date',)

    lease_history = models.ForeignKey(LeaseHistory, on_delete=models.PROTECT)
    transferred_from = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='lease_sales')
    transferred_to = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='lease_purchases')

    original_from = models.CharField(max_length=1024)  # For caching txn data if cust is deleted
    original_to = models.CharField(max_length=1024)  # For caching txn data if cust is deleted
    txn_date = models.DateTimeField(auto_now_add=True, editable=False)
    txn_type = models.CharField(max_length=4, choices=(('BUY', 'BUY'), ('SELL', 'SELL')))
    txn_value = models.DecimalField(max_digits=6, decimal_places=2)
    notes = models.CharField(max_length=10000)

    def __str__(self):
        if self.lease_history.lease:
            return self.lease_history.lease.shortcode
        return self.lease_history.original_lease
