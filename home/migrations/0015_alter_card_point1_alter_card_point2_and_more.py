# Generated by Django 5.0.4 on 2024-05-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_card_heading_alter_card_point1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='point1',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='point2',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='point3',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='point4',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='point5',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
