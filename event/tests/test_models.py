import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestEvent:
    def test_event(self):
        obj = mixer.blend("event.Event")
        assert obj.pk == 1, "Should create an Event instance"
        assert str(obj) == "{} {}".format(obj.name, obj.genre)

    def test_eventsetup(self):
        obj = mixer.blend("event.EventSetUp")
        assert obj.pk == 1, "Should create a EventSetUp instance"
        assert str(obj) == "{} {}".format(obj.business.name, obj.event.name)
