# Generated by Django 5.0.4 on 2024-04-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]