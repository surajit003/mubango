import pytest
from mixer.backend.django import mixer
from common.utils import generate_country_data_for_testing
import datetime
from ..models import Business

pytestmark = pytest.mark.django_db


class TestBusiness:
    def test_business(self):
        obj = mixer.blend("business.Business")
        assert obj.pk == 1, "Should create a Business instance"
        assert str(obj) == "{} {}".format(obj.name, obj.active)

    def test_visitorcount(self):
        obj = mixer.blend("business.VisitorCount")
        assert obj.pk == 1, "Should create a VisitorCount instance"
        assert str(obj) == "{} {}".format(obj.business.name, obj.count)

    def test_service(self):
        obj = mixer.blend("business.Service")
        assert obj.pk == 1, "Should create a Service instance"
        assert str(obj) == "{}".format(obj.name)

    def test_business_service_rating(self):
        obj = mixer.blend("business.BusinessServiceRating")
        assert obj.pk == 1, "Should create a BusinessServiceRating instance"
        assert str(obj) == "{} {} {}".format(
            obj.service.name, obj.business.name, obj.rating
        )


class TestBusinessManager:
    def test_business_manager_get_queryset(self):
        address = generate_country_data_for_testing()
        Business.objects.create(
            name="test",
            email="test@gmail.com",
            active=True,
            phone_number="+254720323305",
            address=address,
            rating=4,
            type="club",
        )

        business = Business.business_manager.top_rated_club("Nairobi")
        assert business.count() == 1

        business = Business.business_manager.closest_clubs("Nairobi")
        assert business.count() == 1

        Business.objects.create(
            name="test",
            email="test@gmail.com",
            active=True,
            phone_number="+254720323305",
            address=address,
            rating=4,
            type="club",
            currently_hot=True,
        )
        business = Business.business_manager.currently_hot_clubs("Nairobi")
        assert business.count() == 1
