from .. import forms
import pytest
from mixer.backend.django import mixer
import datetime

pytestmark = pytest.mark.django_db


class TestOfferForm:
    def test_offer_form_clean(self):
        business = mixer.blend("business.Business")
        form = forms.OfferForm(
            data={
                "code": "1234",
                "business": business.pk,
                "title": "Test offer",
                "start_date": datetime.datetime.now(),
                "limit": 4,
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
                "limit": 3,
            }
        )
        with pytest.raises(ValueError) as ex:
            form1.save()

        business_new = mixer.blend("business.Business")
        form2 = forms.OfferForm(
            data={
                "code": "1234",
                "business": business_new.pk,
                "title": "Test offer",
                "start_date": datetime.datetime.now(),
                "limit": 3,
            }
        )
        instance = form2.save()
        assert instance.title == "Test offer"
