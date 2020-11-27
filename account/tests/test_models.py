import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestUserProfile:
    def test_profile(self):
        obj = mixer.blend("account.Profile")
        assert obj.pk == 1, "Should create a UserProfile instance"
        assert str(obj) == "{} {}".format(obj.user.username, obj.active)

    def test_follower(self):
        obj = mixer.blend("account.Follower")
        assert obj.pk == 1, "Should create a Follower instance"
        assert str(obj) == "{} {}".format(obj.user, obj.follower)
