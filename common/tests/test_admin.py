import pytest
from mixer.backend.django import mixer
from django.contrib.admin.sites import AdminSite
from .. import admin
from .. import models

pytestmark = pytest.mark.django_db


class TestEventAdmin:
    def test_get_event_name(self):
        obj = mixer.blend("common.Address")
        site = AdminSite()
        address_setup_admin = admin.AddressAdmin(models.Address, site)
        result = address_setup_admin.get_country(obj)
        assert result == obj.state.country.name, "Should return the Country name"
