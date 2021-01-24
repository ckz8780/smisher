# Generated by Django 3.1.5 on 2021-01-24 18:13

from django.db import migrations, models
import django.db.models.deletion
import smisher.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0002_auto_20210123_2012'),
        ('shortcodes', '0006_auto_20210124_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_lease', models.CharField(blank=True, max_length=255, null=True)),
                ('lease', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shortcodes.shortcodelease')),
            ],
        ),
        migrations.CreateModel(
            name='LeaseTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_from', models.CharField(max_length=1024)),
                ('original_to', models.CharField(max_length=1024)),
                ('txn_date', models.DateTimeField(auto_now_add=True)),
                ('txn_type', models.CharField(choices=[('BUY', 'BUY'), ('SELL', 'SELL')], max_length=4)),
                ('txn_value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('notes', models.CharField(max_length=10000)),
                ('lease_history', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marketplace.leasehistory')),
                ('transferred_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lease_sales', to='customers.customer')),
                ('transferred_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lease_purchases', to='customers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='LeaseListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.CharField(max_length=10000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField(default=smisher.utils.get_default_expiration)),
                ('is_active', models.BooleanField(default=True)),
                ('lease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing', to='shortcodes.shortcodelease')),
                ('listed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lease_listings', to='customers.customer')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
