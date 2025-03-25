from django.conf import settings
from django.db import models

# Create your models here.


class Events(models.Model):
    EventName = models.CharField(max_length=200, help_text="Event name")
    description = models.TextField(
        blank=True, help_text="Detailed description of the event")
    date = models.DateTimeField(help_text="Date and time of event")
    location = models.CharField(max_length=200, help_text="Event location")

    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name="events", 
        blank=True, 
        help_text="Users participating in this event"
    )


class Guest(models.Model):
    GuestName = models.CharField(max_length=200, help_text="Guest name")
    email = models.EmailField(
        unique=True, help_text="Email address of the guest")

    event = models.ForeignKey(
        "Events",
        on_delete=models.CASCADE,
        related_name="guests",
        help_text="Event the guest is associated with"
    )
