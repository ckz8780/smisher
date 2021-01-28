import uuid
from django.db import models
from customers.models import Customer
from shortcodes.models import ShortCode
from smisher.utils import get_default_expiration

# Create your models here.


class Target(models.Model):

    class Meta:
        ordering = ('phone_number',)

    phone_number = models.PositiveBigIntegerField()
    messages_sent = models.PositiveBigIntegerField()
    replies_received = models.PositiveBigIntegerField()

    def __str__(self):
        return str(self.phone_number)


class Campaign(models.Model):

    class Meta:
        ordering = ('-created_at',)

    campaign_id = models.UUIDField(default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='campaigns')
    shortcode = models.ForeignKey(ShortCode, on_delete=models.CASCADE, related_name='campaign')
    targets = models.ManyToManyField(Target, through='CampaignTarget', related_name='targets')
    sms_provider = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.campaign_id)


class CampaignTarget(models.Model):

    class Meta:
        ordering = ('-created_at',)

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='campaign_targets')
    target = models.ForeignKey(Target, on_delete=models.CASCADE, related_name='campaign_targets')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.target}: {self.campaign}'


class Message(models.Model):

    class Meta:
        ordering = ('-created_at',)

    msg_id = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    target = models.ForeignKey(Target, on_delete=models.CASCADE, related_name='message')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='message')
    msg_content = models.CharField(max_length=10000, null=True, blank=True)
    msg_direction = models.CharField(max_length=3, choices=(('IN', 'IN'), ('OUT', 'OUT')))
    msg_opened = models.BooleanField(default=False)

    def __str__(self):
        return str(self.msg_id)
