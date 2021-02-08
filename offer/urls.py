from django.conf.urls import url
from . import views

app_name = "offer"
urlpatterns = [
    url(
        r"^list-by-region/(?P<region>[\w|\W]+)/$",
        views.OfferListByRegion.as_view(),
        name="get_offer_region",
    ),
    url(
        r"^(?P<slug>[\w-]+)/$",
        views.OfferDetailView.as_view(),
        name="offer_detail",
    ),
    url(
        r"^all/(?P<state>[\w|\W]+)/$",
        views.OfferListView.as_view(),
        name="get_all_offers",
    ),
]
