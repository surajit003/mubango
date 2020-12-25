import pytest
from mixer.backend.django import mixer
from django.contrib.admin.sites import AdminSite
from .. import admin
from .. import models
from mock import patch

pytestmark = pytest.mark.django_db


class TestEventAdmin:
    def test_get_event_name(self):
        event = mixer.blend("event.Event", num_of_tickets=10)
        obj = mixer.blend("event.EventUser", event=event)
        site = AdminSite()
        event_setup_admin = admin.EventUserAdmin(models.EventUser, site)
        result = event_setup_admin.get_event(obj)
        assert result == obj.event.name, "Should return the event name"

    def test_get_user_name(self):
        event = mixer.blend("event.Event", num_of_tickets=10)
        obj = mixer.blend("event.EventUser", event=event)
        site = AdminSite()
        event_user_admin = admin.EventUserAdmin(models.EventUser, site)
        result = event_user_admin.get_user(obj)
        assert result == obj.visitor.username, "Should return the username"
