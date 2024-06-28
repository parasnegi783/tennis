# Generated by Django 5.0.4 on 2024-06-19 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_participants'),
    ]

    operations = [
        migrations.CreateModel(
            name='second_event_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='first_event_category',
        ),
        migrations.CreateModel(
            name='first_event_name',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=220, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_event_name', to='home.first_event_category')),
            ],
        ),
        migrations.CreateModel(
            name='second_event_name',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=220, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_event_name', to='home.second_event_category')),
            ],
        ),
        migrations.DeleteModel(
            name='Participants',
        ),
    ]