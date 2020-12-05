import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestEvent:
    def test_event(self):
        obj = mixer.blend("event.Event")
        assert obj.pk == 1, "Should create an Event instance"
        assert str(obj) == "{} {}".format(obj.name, obj.genre)

    def test_clubevent(self):
        obj = mixer.blend("event.ClubEvent")
        assert obj.pk == 1, "Should create a ClubEvent instance"
        assert str(obj) == "{} {}".format(obj.club.name, obj.event.name)

    def test_independentevent(self):
        obj = mixer.blend("event.IndependentEvent")
        assert obj.pk == 1, "Should create a IndependentEvent instance"
        assert str(obj) == "{} {} {}".format(
            obj.event.name, obj.venue.name, obj.venue.address.country
        )
