from django.conf.urls import url
from . import views

app_name = "business"
urlpatterns = [
    url(
        r"^search/(?P<city>[\w-]+)/$",
        views.search_for_business,
        name="search_business",
    ),
]
