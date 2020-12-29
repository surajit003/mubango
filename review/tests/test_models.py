import pytest
from mixer.backend.django import mixer
from ..models import Review
from django.contrib.auth.models import User

pytestmark = pytest.mark.django_db


class TestReview:
    def test_review(self):
        obj = mixer.blend("review.Review")
        assert obj.pk == 1, "Should create a Rating instance"
        assert str(obj) == "{} {} {}".format(
            obj.id, obj.user.username, obj.business.name
        )

    def test_conv_star_to_number(self):
        obj = mixer.blend("review.Review")
        obj.conv_star_to_rating("*")
        assert obj.ratings == 1
        obj.conv_star_to_rating("**")
        assert obj.ratings == 2
        obj.conv_star_to_rating("***")
        assert obj.ratings == 3
        obj.conv_star_to_rating("****")
        assert obj.ratings == 4
        obj.conv_star_to_rating("*****")
        assert obj.ratings == 5


class TestOfferManager:
    def test_review_manager_get_queryset(self):
        business = mixer.blend("business.Business", name="PBP")
        user = mixer.blend(User, username="rj001")
        mixer.blend("review.Review", business=business, user=user, moderated=True)
        assert (
            Review.review_manager.get_review_for_a_specific_user("rj001").count() == 1
        )
        assert Review.review_manager.review_for_a_business("PBP").count() == 1
