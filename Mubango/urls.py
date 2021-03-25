"""Mubango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
from django.contrib.auth import views as auth_views

app_name = "mubango"
main = [
    url(r"^logout/", auth_views.LogoutView.as_view(), name="logout"),
    url(r"^account/", include("account.urls")),
    url(r"^business/", include("business.urls")),
    url(r"^event/", include("event.urls")),
    url(r"^offer/", include("offer.urls")),
    url(r"", include("core.urls")),
    url(r"^social-auth/", include("social_django.urls", namespace="social")),
    url(r"^admin/", admin.site.urls),
    url(r"^__debug__/", include(debug_toolbar.urls)),
]

urlpatterns = (
    [url(r"^mb/", include(main))]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

admin.site.site_header = "Mubango Admin"
admin.site.site_title = "Mubango Admin Portal"
admin.site.index_title = "Welcome to Mubango Admin Portal"


def show_toolbar(request):
    return True


SHOW_TOOLBAR_CALLBACK = show_toolbar
