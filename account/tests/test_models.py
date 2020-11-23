import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestUserProfile:
    def test_profile(self):
        obj = mixer.blend("account.Profile")
        assert obj.pk == 1, "Should create a UserProfile instance"
        assert str(obj) == "{} {}".format(obj.user.username, obj.active)

    def test_country(self):
        obj = mixer.blend("account.Country")
        assert obj.pk == 1, "Should create a Country instance"
        assert str(obj) == obj.country.name

    def test_state(self):
        obj = mixer.blend("account.State")
        assert obj.pk == 1, "Should create a State instance"
        assert str(obj) == obj.name

    def test_city(self):
        obj = mixer.blend("account.City")
        assert obj.pk == 1, "Should create a City instance"
        assert str(obj) == obj.name

    def test_address(self):
        obj = mixer.blend("account.Address")
        assert obj.pk == 1, "Should create an Address instance"
        assert str(obj) == obj.location

    def test_follower(self):
        obj = mixer.blend("account.Follower")
        assert obj.pk == 1, "Should create a Follower instance"
        assert str(obj) == "{} {}".format(obj.user, obj.follower)
