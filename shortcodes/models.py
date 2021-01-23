from django.db import models
from customers.models import Customer

# Create your models here.
class ShortCode(models.Model):
  shortcode = models.PositiveBigIntegerField()
  description = models.CharField(max_length=10000, default=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  is_available = models.BooleanField(default=True)
  available_on = models.DateTimeField(blank=True, null=True)


class ShortCodeLease(models.Model):
  leased_to = models.ForeignKey(Customer, on_delete=models.CASCADE)
  shortcode = models.OneToOneField(ShortCode, on_delete=models.CASCADE)
  description = models.CharField(max_length=10000, default=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  expires_at = models.DateTimeField(auto_now_add=True)
  is_active = models.BooleanField(default=False)