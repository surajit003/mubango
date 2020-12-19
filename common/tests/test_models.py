import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestUserProfile:
    def test_rating(self):
        obj = mixer.blend("common.Rating")
        assert obj.pk == 1, "Should create a Rating instance"
        assert str(obj) == "{} {}".format(obj.name, obj.symbol)

    def test_guest(self):
        obj = mixer.blend("common.Guest")
        assert obj.pk == 1, "Should create an Guest instance"
        assert str(obj) == "{} {}".format(obj.first_name, obj.last_name)

    def test_musicgenre(self):
        obj = mixer.blend("common.MusicGenre")
        assert obj.pk == 1, "Should create a MusicGenre instance"
        assert str(obj) == "{}".format(obj.name)

    def test_venue(self):
        obj = mixer.blend("common.Venue")
        assert obj.pk == 1, "Should create a Venue instance"
        assert str(obj) == "{} {}".format(obj.name, obj.description)
