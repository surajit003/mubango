from django.conf.urls import url
from . import views

app_name = "business"
urlpatterns = [
    url(
        r"^search-all/(?P<state>[\w-]+)/$",
        views.get_all_business,
        name="get_all_business",
    ),
    url(
        r"^search-single/(?P<name>[\w|\W]+)/(?P<state>[\w-]+)/$",
        views.search_for_a_specific_business,
        name="search_for_a_specific_business",
    ),
    url(
        r"^all/(?P<state>[\w|\W]+)/$",
        views.ClubListView.as_view(),
        name="get_all_clubs",
    ),
    url(
        r"^(?P<slug>[\w-]+)/$",
        views.ClubDetailView.as_view(),
        name="club_detail",
    ),
]
