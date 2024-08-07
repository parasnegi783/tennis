# Generated by Django 5.0.4 on 2024-07-04 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_eventcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamForFirstEvent',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.participant')),
                ('second_partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.participant')),
            ],
        ),
        migrations.CreateModel(
            name='TeamForSecondEvent',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('second_partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.participant')),
            ],
        ),
        migrations.DeleteModel(
            name='EventCategory',
        ),
    ]
