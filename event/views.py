from django.shortcuts import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Event, EventSocial, EventImage, EventServiceRating
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

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context["event_social"] = EventSocial.objects.filter(
            event__slug=self.kwargs.get("slug"), active=True
        )
        context["gallery"] = EventImage.objects.filter(
            event__slug=self.kwargs.get("slug"), img_category="other"
        )
        context["event_amenities"] = EventServiceRating.objects.filter(
            event__slug=self.kwargs.get("slug")
        ).select_related("service")
        return context


class EventListView(ListView):
    paginate_by = 16
    model = Event
    template_name = "event/event_list.html"

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        event_list = Event.event_manager.upcoming_events(self.kwargs.get("state"))
        context["event_list"] = event_list
        return context
