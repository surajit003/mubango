from django.test import RequestFactory
import pytest
from .. import views
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestIndexView:
    def test_indexview(self):
        path = reverse("core:home")
        request = RequestFactory().get(path)
        response = views.Index(request)
        assert response.status_code == 200, "Should return 200"
