# Generated by Django 5.0.4 on 2024-06-19 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_rename_event_id_firsteventname_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='firsteventname',
            name='event_id',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AddField(
            model_name='secondeventname',
            name='event_id',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
