import pytest
from mixer.backend.django import mixer
from django.contrib.admin.sites import AdminSite
from .. import admin
from .. import models

pytestmark = pytest.mark.django_db


class TestClubAdmin:
    def test_get_address(self):
        obj = mixer.blend("club.Club")
        site = AdminSite()
        club_admin = admin.ClubAdmin(models.Club, site)
        result = club_admin.get_address(obj)
        assert result == obj.address.location, "Should return the location value"

    def test_get_address_for_event(self):
        obj = mixer.blend("club.IndependentEvent")
        site = AdminSite()
        club_admin = admin.IndependentEventAdmin(models.IndependentEvent, site)
        result = club_admin.get_address(obj)
        assert result == obj.address.location, "Should return the location value"

    def test_get_country(self):
        obj = mixer.blend("club.IndependentEvent")
        site = AdminSite()
        independent_event_admin = admin.IndependentEventAdmin(
            models.IndependentEvent, site
        )
        result = independent_event_admin.get_country(obj)
        assert result == obj.address.country, "Should return the country value"

    def test_get_event(self):
        obj = mixer.blend("club.IndependentEvent")
        site = AdminSite()
        independent_event_admin = admin.IndependentEventAdmin(
            models.IndependentEvent, site
        )
        result = independent_event_admin.get_event(obj)
        assert result == obj.event.name, "Should return the event value"

    def test_get_club_event(self):
        obj = mixer.blend("club.ClubEvent")
        site = AdminSite()
        independent_event_admin = admin.ClubEventAdmin(models.ClubEvent, site)
        result = independent_event_admin.get_event(obj)
        assert result == obj.event.name, "Should return the event value"

    def test_get_club_name(self):
        obj = mixer.blend("club.ClubEvent")
        site = AdminSite()
        independent_event_admin = admin.ClubEventAdmin(models.ClubEvent, site)
        result = independent_event_admin.get_club(obj)
        assert result == obj.club.name, "Should return the event value"
