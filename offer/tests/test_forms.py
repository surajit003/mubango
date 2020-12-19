from .. import forms
import pytest
from mixer.backend.django import mixer
import datetime

pytestmark = pytest.mark.django_db


class TestOfferForm:
    def test_form(self):
        business = mixer.blend("business.Business")
        form = forms.OfferForm(
            data={
                "code": "1234",
                "business": business.pk,
                "title": "Test offer",
                "start_date": datetime.datetime.now(),
            }
        )
        instance = form.save()
        assert instance.title == "Test offer"
        form1 = forms.OfferForm(
            data={
                "code": "1234",
                "business": business.pk,
                "title": "Test offer",
                "start_date": datetime.datetime.now(),
            }
        )
        with pytest.raises(ValueError) as ex:
            form1.save()
