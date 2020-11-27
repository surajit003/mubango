import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestClub:
    def test_club(self):
        obj = mixer.blend("club.Club")
        assert obj.pk == 1, "Should create a Club instance"
        assert str(obj) == "{} {}".format(obj.name, obj.active)
