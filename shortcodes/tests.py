from django.test import TestCase
from .models import ShortCode, ShortCodeLease
from customers.models import Customer
from datetime import timedelta
from django.utils import timezone

# Create your tests here.


class TestShortCodes(TestCase):

    def test_shortcode_defaults_to_available(self):
        sc = ShortCode.objects.create(shortcode=12345)
        self.assertTrue(sc.is_available)

    def test_shortcode_updated_on_lease_creation(self):
        sc = ShortCode.objects.create(shortcode=12345)
        cust = Customer.objects.create(cust_name='test_customer')
        lease = ShortCodeLease.objects.create(leased_to=cust, shortcode=sc)
        self.assertFalse(sc.is_available)

    def test_shortcode_updated_on_lease_status_change(self):
        sc = ShortCode.objects.create(shortcode=12345)
        cust = Customer.objects.create(cust_name='test_customer')
        lease = ShortCodeLease.objects.create(leased_to=cust, shortcode=sc)
        self.assertFalse(sc.is_available)
        lease.deactivate()
        self.assertTrue(sc.is_available)


class TestLeases(TestCase):

    def test_lease_default_term_is_30_days(self):
        sc = ShortCode.objects.create(shortcode=12345)
        cust = Customer.objects.create(cust_name='test_customer')
        lease = ShortCodeLease.objects.create(leased_to=cust, shortcode=sc)
        test_date = timezone.now() + timedelta(days=30)
        self.assertAlmostEqual(lease.expires_at.date(), test_date.date())
