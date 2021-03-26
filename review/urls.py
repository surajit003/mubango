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
    url(
        r"^all/$",
        login_required(views.ReviewList.as_view()),
        name="user_review_list",
    ),
    url(
        r"^update/(?P<pk>[\w|\W]+)/$",
        login_required(views.ReviewUpdate.as_view()),
        name="user_update",
    ),
    url(
        r"^delete/(?P<pk>[\w|\W]+)/$",
        login_required(views.ReviewDeleteView.as_view()),
        name="review_delete",
    ),
]
