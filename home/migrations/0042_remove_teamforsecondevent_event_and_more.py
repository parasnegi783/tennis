# Generated by Django 5.0.4 on 2024-07-09 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_category_alter_teamforfirstevent_first_partner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamforsecondevent',
            name='event',
        ),
        migrations.RemoveField(
            model_name='teamforfirstevent',
            name='event',
        ),
        migrations.DeleteModel(
            name='category',
        ),
    ]
