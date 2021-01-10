from django.shortcuts import HttpResponse
from django.views.generic import DetailView
from .models import Event
import json


# Create your views here.


def search_for_a_specific_event(request, name, state):
    if request.method == "GET":
        response = [
            obj.as_dict() for obj in Event.event_manager.get_specific_event(name, state)
        ]
        return HttpResponse(
            json.dumps({"data": response}), content_type="application/json"
        )


def get_all_events_in_a_state(request, state):
    if request.method == "GET":
        response = [obj.as_dict() for obj in Event.event_manager.upcoming_events(state)]
        return HttpResponse(
            json.dumps({"data": response}), content_type="application/json"
        )


class EventDetailView(DetailView):
    model = Event
    template_name = "event/event_detail.html"
