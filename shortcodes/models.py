from django.db import models
from customers.models import Customer
from datetime import timedelta
from django.utils import timezone


# Create your models here.
class ShortCode(models.Model):

    class Meta:
        ordering = ('shortcode',)

    shortcode = models.PositiveBigIntegerField()
    description = models.CharField(max_length=10000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    available_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.shortcode)


class ShortCodeLease(models.Model):

    class Meta:
        ordering = ('shortcode',)

    def _get_default_expiration():
        return timezone.now() + timedelta(days=30)

    leased_to = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shortcode = models.OneToOneField(ShortCode, on_delete=models.CASCADE, related_name='lease')
    description = models.CharField(max_length=10000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=_get_default_expiration)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.shortcode.is_available = False if self.is_active else True
        self.shortcode.available_on = self.expires_at if self.is_active else None
        self.shortcode.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.shortcode}: {self.leased_to.cust_name}'
