import pytest
from mixer.backend.django import mixer
from ..models import Event
import datetime
from common.utils import generate_country_data_for_testing

pytestmark = pytest.mark.django_db


class TestEvent:
    def test_event(self):
        obj = mixer.blend("event.Event")
        assert obj.pk == 1, "Should create an Event instance"
        assert str(obj) == "{} {}".format(obj.name, obj.genre)

    def test_eventsetup(self):
        event = mixer.blend("event.Event", num_of_tickets=10)
        obj = mixer.blend("event.EventUser", event=event)
        assert obj.pk == 1, "Should create a EventUser instance"
        assert str(obj) == "{} {}".format(obj.event.name, obj.visitor.username)

    def test_event_user_for_no_available_tickets(self):
        event = mixer.blend("event.Event", limit=0)
        with pytest.raises(Exception):
            mixer.blend("event.EventUser", event=event)


class TestEventManager:
    def test_event_manager_get_queryset(self):
        address = generate_country_data_for_testing()
        dt = datetime.date.today()

        business = mixer.blend("business.Business", address=address)
        event = Event.event_manager.create(
            name="test",
            to_be_held_on=dt,
            active=True,
            location=address,
        )
        event.business.add(business)
        event.save()
        assert event.id == 1

        event = Event.event_manager.upcoming_events("Nairobi")
        assert event.count() == 1

        event = Event.event_manager.create(
            name="test",
            to_be_held_on=dt,
            active=True,
            location=address,
            is_special=True,
        )
        event.business.add(business)
        event.save()
        ev = Event.event_manager.upcoming_special_events("Nairobi")
        assert ev.count() == 1
