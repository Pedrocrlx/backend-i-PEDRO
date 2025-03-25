from django.contrib import admin
from .models import Events, Guest

# Register the Event model
@admin.register(Events)
class Event(admin.ModelAdmin):
    list_display = ('EventName', 'date', 'location')  # Columns to display in the admin panel
    search_fields = ('EventName', 'location')  # Enable search functionality
    list_filter = ('date', 'location')  # Add filters in the sidebar
    ordering = ('date',)  # Default ordering by date

# Register the Guest model
@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('GuestName', 'email', 'event')  # Columns for Guest model
    search_fields = ('GuestName', 'email')  # Enable search functionality
    list_filter = ('event',)  # Filter by associated event
    ordering = ('GuestName',)  # Default ordering by guest name
