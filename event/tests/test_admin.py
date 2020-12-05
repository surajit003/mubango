import pytest
from mixer.backend.django import mixer
from django.contrib.admin.sites import AdminSite
from .. import admin
from .. import models

pytestmark = pytest.mark.django_db


class TestEventAdmin:
    def test_get_club_event(self):
        obj = mixer.blend("event.EventSetUp")
        site = AdminSite()
        event_setup_admin = admin.EventSetUpAdmin(models.EventSetUp, site)
        result = event_setup_admin.get_event(obj)
        assert result == obj.event.name, "Should return the event value"

    def test_get_club_name(self):
        obj = mixer.blend("event.EventSetUp")
        site = AdminSite()
        event_setup_admin = admin.EventSetUpAdmin(models.EventSetUp, site)
        result = event_setup_admin.get_business(obj)
        assert result == obj.business.name, "Should return the event value"
