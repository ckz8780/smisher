# Generated by Django 3.1.5 on 2021-01-24 01:12

from django.db import migrations, models
import shortcodes.models


class Migration(migrations.Migration):

    dependencies = [
        ('shortcodes', '0002_auto_20210122_2154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shortcode',
            options={'ordering': ('shortcode',)},
        ),
        migrations.AlterModelOptions(
            name='shortcodelease',
            options={'ordering': ('shortcode',)},
        ),
    ]
