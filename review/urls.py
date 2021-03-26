from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = "review"
urlpatterns = [
    url(
        r"^add-review/$",
        login_required(views.save_review),
        name="save_review",
    ),
    url(
        r"^service/rating/$",
        login_required(views.add_service_rating),
        name="save_review",
    ),
]
