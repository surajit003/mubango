from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = "account"

urlpatterns = [
    url(r"^home", views.Home, name="home"),
    url(r"^login", views.LoginView, name="login"),
    url(r"^logout", views.LogoutView, name="logout"),
    url(r"^signup", views.SignupView, name="signup"),
    url(
        r"^ajax/validate_username/$", views.validate_username, name="validate_username"
    ),
    url(
        r"^ajax/validate_phonenumber/$",
        views.validate_phonenumber,
        name="validate_phone",
    ),
    url(r"^ajax/validate_email/$", views.validate_email, name="validate_email"),
    url(r"^ajax/validate_email/$", views.validate_email, name="validate_email"),
    url(
        r"^profile/(?P<slug>[0-9a-f-]+)/$",
        login_required(views.ProfileDetail.as_view()),
        name="profile_detail",
    ),
    url(
        r"^profile/(?P<slug>[0-9a-f-]+)/update/$",
        login_required(views.UpdateProfile),
        name="profile_update",
    ),
    url(
        r"^password/(?P<slug>[0-9a-f-]+)/update/$",
        login_required(views.UpdatePassword),
        name="password_update",
    ),
]
