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
