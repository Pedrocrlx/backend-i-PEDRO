from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    path('', views.events_list, name='events_list'),  # Lists all events
    path('<int:event_id>/', views.event_detail, name='event_detail'),  # Event details
]
