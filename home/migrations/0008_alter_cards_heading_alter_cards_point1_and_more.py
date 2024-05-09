# Generated by Django 5.0.4 on 2024-05-06 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_cards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='heading',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cards',
            name='point1',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='cards',
            name='point2',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='cards',
            name='point3',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='cards',
            name='point4',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='cards',
            name='point5',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
    ]
