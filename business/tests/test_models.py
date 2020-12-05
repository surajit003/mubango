import pytest
from mixer.backend.django import mixer

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

    def test_trending(self):
        obj = mixer.blend("business.Trending")
        assert obj.pk == 1, "Should create a Trending instance"
        assert str(obj) == "{} {}".format(obj.business.name, obj.thumbs_up_count)
