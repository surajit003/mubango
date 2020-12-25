import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestReview:
    def test_review(self):
        obj = mixer.blend("review.Review")
        assert obj.pk == 1, "Should create a Rating instance"
        assert str(obj) == "{} {} {}".format(
            obj.id, obj.user.username, obj.business.name
        )
