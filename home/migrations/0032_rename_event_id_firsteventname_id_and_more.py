# Generated by Django 5.0.4 on 2024-06-19 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_remove_second_event_name_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firsteventname',
            old_name='event_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='secondeventname',
            old_name='event_id',
            new_name='id',
        ),
    ]
