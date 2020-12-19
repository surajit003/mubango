import pytest
from mixer.backend.django import mixer
from django.contrib.admin.sites import AdminSite
from .. import admin
from .. import models

pytestmark = pytest.mark.django_db


class TestOfferAdmin:
    def test_business_name(self):
        obj = mixer.blend("offer.Offer")
        site = AdminSite()
        offer_setup_admin = admin.OfferAdmin(models.Offer, site)
        result = offer_setup_admin.get_business_name(obj)
        assert result == obj.business.name, "Should return the business name"
