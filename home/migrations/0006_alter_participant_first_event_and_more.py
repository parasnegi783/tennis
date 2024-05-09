# Generated by Django 5.0.4 on 2024-05-05 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_p1_food_preference_secondevent_p2_food_preference_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='first_event',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.firstevent'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='second_event',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.secondevent'),
        ),
    ]
