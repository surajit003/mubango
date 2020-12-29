import pytest
from mock import patch
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from account.models import Profile
from datetime import datetime

pytestmark = pytest.mark.django_db


class TestUserProfile:
    def test_profile(self):
        obj = mixer.blend("account.Profile")
        assert obj.pk == 1, "Should create a UserProfile instance"
        assert str(obj) == "{} {}".format(obj.user.username, obj.active)

    @patch("account.signals.create_profile")
    def test_follower(self, mock_handler):
        obj = mixer.blend("account.Follower")
        assert mock_handler.call_count == 2  # standard django
        assert obj.pk == 1, "Should create a Follower instance"
        assert str(obj) == "{} {}".format(obj.user, obj.follower)

    def test_profile_creation(self):
        user = mixer.blend(User)
        profile = Profile.objects.filter(user=user)
        assert profile.count() == 1, "Should create a profile instance"

    def test_months_on_mubango(self):
        user = mixer.blend(User)
        profile = Profile.objects.get(user=user)
        profile.verification_id = "29"
        profile.save()
        assert profile.months_on_mubango() == "{}:{}".format("days", 0)

        user = mixer.blend(User, date_joined=datetime(year=2020, month=3, day=1))
        profile = Profile.objects.get(user=user)
        profile.verification_id = "90"
        profile.save()
        user_joined = user.date_joined.replace(tzinfo=None)
        d = datetime.now()
        diff = abs(d - user_joined)
        days = diff.days
        month = int(round(days / 30))
        assert profile.months_on_mubango() == "{}:{}".format("months", month)
