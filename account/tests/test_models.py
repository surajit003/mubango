import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestUserProfile:
    def test_user_profile(self):
        obj = mixer.blend("account.Profile")
        assert obj.pk == 1, "Should create a UserProfile instance"

    def test_country(self):
        obj = mixer.blend("account.Country")
        assert obj.pk == 1, "Should create a Country instance"

    def test_state(self):
        obj = mixer.blend("account.State")
        assert obj.pk == 1, "Should create a State instance"

    def test_city(self):
        obj = mixer.blend("account.City")
        assert obj.pk == 1, "Should create a City instance"

    def test_address(self):
        obj = mixer.blend("account.Address")
        assert obj.pk == 1, "Should create an Address instance"
