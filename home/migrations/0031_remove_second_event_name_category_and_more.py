# Generated by Django 5.0.4 on 2024-06-19 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_second_event_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='second_event_name',
            name='category',
        ),
        migrations.RenameModel(
            old_name='first_event_category',
            new_name='FirstEventCategory',
        ),
        migrations.CreateModel(
            name='FirstEventName',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=220, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_event_names', to='home.firsteventcategory')),
            ],
        ),
        migrations.RenameModel(
            old_name='second_event_category',
            new_name='SecondEventCategory',
        ),
        migrations.CreateModel(
            name='SecondEventName',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=220, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_event_names', to='home.secondeventcategory')),
            ],
        ),
        migrations.DeleteModel(
            name='first_event_name',
        ),
        migrations.DeleteModel(
            name='second_event_name',
        ),
    ]