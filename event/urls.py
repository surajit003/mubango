from django.conf.urls import url
from . import views

app_name = "Event"
urlpatterns = [
    url(
        r"^search-single/(?P<name>[\w|\W]+)/(?P<state>[\w-]+)/$",
        views.search_for_a_specific_event,
        name="search_for_a_specific_event",
    ),
    url(
        r"^search-all/(?P<state>[\w-]+)/$",
        views.get_all_events_in_a_state,
        name="get_all_events",
    ),
]
