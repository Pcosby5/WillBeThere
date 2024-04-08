# Generated by Django 5.0.4 on 2024-04-08 15:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=200)),
                ('eventImageUrl', models.URLField()),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('congratulatoryMessage', models.TextField(blank=True, null=True)),
                ('items', models.JSONField()),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('attending', models.BooleanField()),
                ('additionalPeople', models.JSONField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventsPlanner.event')),
            ],
        ),
    ]