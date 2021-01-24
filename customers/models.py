from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):

    class Meta:
        ordering = ('cust_name',)

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    cust_name = models.CharField(max_length=1024)

    def __str__(self):
        return f'{self.cust_name} ({self.user})'
