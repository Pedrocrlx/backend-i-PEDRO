# Generated by Django 5.1.7 on 2025-03-25 13:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EventManagement", "0002_alter_events_eventname_guest"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="events",
            name="participants",
            field=models.ManyToManyField(
                blank=True,
                help_text="Users participating in this event",
                related_name="events",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
