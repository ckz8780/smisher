from django.contrib import admin
from .models import Campaign, Target, CampaignTarget, Message


class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        'campaign_id',
        'created_by',
        'shortcode',
        'sms_provider',
        'created_at',
        'start_date',
        'end_date',
    )


class TargetAdmin(admin.ModelAdmin):
    list_display = (
        'phone_number',
        'messages_sent',
        'replies_received',
    )


class CampaignTargetAdmin(admin.ModelAdmin):
    list_display = (
        'campaign',
        'target',
        'created_at',
    )


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'campaign',
        'target',
        'msg_direction',
        'msg_opened',
        'msg_content',
        'msg_id',
    )


# Register your models here.
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Target, TargetAdmin)
admin.site.register(CampaignTarget, CampaignTargetAdmin)
admin.site.register(Message, MessageAdmin)
