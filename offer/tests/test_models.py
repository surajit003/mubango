import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestOffer:
    def test_offer(self):
        obj = mixer.blend("offer.Offer")
        assert obj.pk == 1, "Should create a Offer instance"
        assert str(obj) == "{} {}".format(obj.title, obj.business.name)
