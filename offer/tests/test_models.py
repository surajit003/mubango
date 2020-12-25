import pytest
from mixer.backend.django import mixer
from mock import patch
from ..models import Offer
from common.utils import generate_country_data_for_testing
import datetime
import pytz

pytestmark = pytest.mark.django_db


class TestOffer:
    def test_offer(self):
        obj = mixer.blend("offer.Offer")
        assert obj.pk == 1, "Should create a Offer instance"
        assert str(obj) == "{}".format(obj.title)


class TestUserOffer:
    def test_user_offer(self):
        offer = mixer.blend("offer.Offer", limit=10)
        obj = mixer.blend("offer.UserOffer", offer=offer)
        assert str(obj) == "{}".format(obj.offer.title)

    def test_user_offer_for_valid_limit(self):
        offer = mixer.blend("offer.Offer", limit=10)
        obj = mixer.blend("offer.UserOffer", offer=offer)
        assert obj.pk == 1, "Should create a UserOffer instance"

    def test_user_offer_for_invalid_limit(self):
        offer = mixer.blend("offer.Offer", limit=0)
        with pytest.raises(Exception):
            mixer.blend("offer.UserOffer", offer=offer)

    # usermodel instance creation without triggering signals
    @patch("offer.signals.validate_and_update_offer_limit")
    def test_signals_with_mock(self, mock_handler):
        offer = mixer.blend("offer.Offer", limit=0)
        obj = mixer.blend("offer.UserOffer", offer=offer)
        assert mock_handler.call_count == 1  # standard django
        assert obj.pk == 1, "Should create a UserOffer instance"


class TestOfferManager:
    def test_offer_manager_get_queryset(self):
        address = generate_country_data_for_testing()
        dt = datetime.datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC)

        business = mixer.blend("business.Business", address=address)
        off = Offer.user_offer.create(
            title="test",
            business=business,
            start_date=dt,
            active=True,
            location=address,
        )
        assert off.id == 1

        off = Offer.user_offer.top_five_offer_based_on_user_state("Nairobi")
        assert off.count() == 1

        user_location = [-1.0, 30.12]
        off = Offer.user_offer.top_five_closest_offer_based_on_user_geolocation(
            "Nairobi", user_location
        )
        assert len(off) == 1
