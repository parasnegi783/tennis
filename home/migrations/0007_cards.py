# Generated by Django 5.0.4 on 2024-05-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_participant_first_event_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(default=None, max_length=120, null=True)),
                ('point1', models.CharField(default=None, max_length=120, null=True)),
                ('point2', models.CharField(default=None, max_length=120, null=True)),
                ('point3', models.CharField(default=None, max_length=120, null=True)),
                ('point4', models.CharField(default=None, max_length=120, null=True)),
                ('point5', models.CharField(default=None, max_length=120, null=True)),
            ],
        ),
    ]
