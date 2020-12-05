import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestClub:
    def test_club(self):
        obj = mixer.blend("club.Club")
        assert obj.pk == 1, "Should create a Club instance"
        assert str(obj) == "{} {}".format(obj.name, obj.active)

    def test_visitorcount(self):
        obj = mixer.blend("club.VisitorCount")
        assert obj.pk == 1, "Should create a VisitorCount instance"
        assert str(obj) == "{} {}".format(obj.club.name, obj.count)

    def test_trending(self):
        obj = mixer.blend("club.Trending")
        assert obj.pk == 1, "Should create a Trending instance"
        assert str(obj) == "{} {}".format(obj.club.name, obj.thumbs_up_count)
