# Generated by Django 5.0.4 on 2024-05-06 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_cards_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='heading',
            field=models.CharField(default=None, max_length=15, null=True),
        ),
    ]
