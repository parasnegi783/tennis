# Generated by Django 5.0.4 on 2024-07-09 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_remove_teamforsecondevent_event_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='teamforfirstevent',
            name='event',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='first_event_teams', to='home.category'),
        ),
        migrations.AddField(
            model_name='teamforsecondevent',
            name='event',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='second_event_teams', to='home.category'),
        ),
    ]
