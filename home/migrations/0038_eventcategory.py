# Generated by Django 5.0.4 on 2024-07-04 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_bankdetail_event_paymentinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('first', 'First Event'), ('second', 'Second Event')], max_length=6)),
                ('category', models.CharField(default=None, max_length=20, null=True)),
                ('partner', models.CharField(default=None, max_length=20, null=True)),
                ('event_id', models.CharField(default=None, max_length=20, null=True)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.participant')),
            ],
            options={
                'unique_together': {('participant', 'event_type')},
            },
        ),
    ]