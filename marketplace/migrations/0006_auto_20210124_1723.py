# Generated by Django 3.1.5 on 2021-01-24 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0005_auto_20210124_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaselisting',
            name='lease_expires',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]