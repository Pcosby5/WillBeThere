# Generated by Django 5.0.4 on 2024-04-09 03:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsPlanner', '0004_alter_rsvp_additionalpeople'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='items',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='additionalPeople',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='items',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None),
        ),
    ]