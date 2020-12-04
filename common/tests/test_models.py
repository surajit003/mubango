import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestUserProfile:
    def test_country(self):
        obj = mixer.blend("common.Country")
        assert obj.pk == 1, "Should create a Country instance"
        assert str(obj) == obj.country.name

    def test_state(self):
        obj = mixer.blend("common.State")
        assert obj.pk == 1, "Should create a State instance"
        assert str(obj) == obj.name

    def test_city(self):
        obj = mixer.blend("common.City")
        assert obj.pk == 1, "Should create a City instance"
        assert str(obj) == obj.name

    def test_address(self):
        obj = mixer.blend("common.Address")
        assert obj.pk == 1, "Should create an Address instance"
        assert str(obj) == obj.location

    def test_rating(self):
        obj = mixer.blend("common.Rating")
        assert obj.pk == 1, "Should create a Rating instance"
        assert str(obj) == "{} {}".format(obj.name, obj.symbol)