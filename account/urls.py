from django.conf.urls import url
from . import views

app_name = "account"

urlpatterns = [
    url(r"^home", views.home, name="home"),
    url(r"^login", views.loginview, name="login"),
    url(r"^signup", views.signupview, name="signup"),
    url(
        r"^ajax/validate_username/$", views.validate_username, name="validate_username"
    ),
    url(
        r"^ajax/validate_phonenumber/$",
        views.validate_phonenumber,
        name="validate_phone",
    ),
    url(r"^ajax/validate_email/$", views.validate_email, name="validate_email"),
]
