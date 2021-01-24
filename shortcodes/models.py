from django.db import models
from customers.models import Customer

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

    leased_to = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shortcode = models.OneToOneField(ShortCode, on_delete=models.CASCADE)
    description = models.CharField(max_length=10000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.shortcode}: {self.leased_to.cust_name}'
