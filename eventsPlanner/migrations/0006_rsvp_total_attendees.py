# Generated by Django 5.0.4 on 2024-04-09 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsPlanner', '0005_alter_event_items_alter_rsvp_additionalpeople_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='total_attendees',
            field=models.IntegerField(default=1),
        ),
    ]
