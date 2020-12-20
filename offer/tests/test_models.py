import pytest
from mixer.backend.django import mixer
from mock import patch

pytestmark = pytest.mark.django_db


class TestOffer:
    def test_offer(self):
        obj = mixer.blend("offer.Offer")
        assert obj.pk == 1, "Should create a Offer instance"
        assert str(obj) == "{}".format(obj.title)


class TestUserOffer:
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
