# Generated by Django 5.0.4 on 2024-05-05 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_firstevent_p1_indian_tree_shorts_size_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secondevent',
            old_name='p1_food_preference',
            new_name='p2_food_preference',
        ),
        migrations.RenameField(
            model_name='secondevent',
            old_name='p1_indian_tree_shorts_size',
            new_name='p2_indian_tree_shorts_size',
        ),
        migrations.RenameField(
            model_name='secondevent',
            old_name='p1_indian_tree_tshirt_size',
            new_name='p2_indian_tree_tshirt_size',
        ),
        migrations.RenameField(
            model_name='secondevent',
            old_name='p1_stay_arrangement',
            new_name='p2_stay_arrangement',
        ),
    ]
