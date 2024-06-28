# Generated by Django 5.0.4 on 2024-06-25 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_remove_paymentinfo_bank_detail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=20)),
                ('ifsc_code', models.CharField(max_length=20)),
                ('bank_name', models.CharField(max_length=100)),
                ('branch_name', models.CharField(max_length=100)),
                ('qr_code_image', models.ImageField(upload_to='qr_codes/')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('bank_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bankdetail')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.event')),
            ],
        ),
    ]