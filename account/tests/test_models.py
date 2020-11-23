import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestUserProfile:
    def test_user_profile(self):
        obj = mixer.blend("account.Profile")
        assert obj.pk == 1, "Should create a UserProfile instance"

    def test_country(self):
        obj = mixer.blend("account.Country")
        assert  obj.pk==1, "Should create a Country instance"
