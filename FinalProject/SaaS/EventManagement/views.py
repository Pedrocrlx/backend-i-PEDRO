from django.shortcuts import get_object_or_404, render
from .models import Events

# Create your views here.

def events_list(request):
    events = Events.objects.all()  # Fetch all events from the database
    return render(request, 'events/events_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Events, id=event_id)  # Fetch the event by ID
    return render(request, 'events/event_detail.html', {'event': event})
