# Generated by Django 5.0.4 on 2024-05-06 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_cards_heading_alter_cards_point1_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cards',
            new_name='card',
        ),
    ]
