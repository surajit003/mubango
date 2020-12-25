from .. import forms
import pytest
from mixer.backend.django import mixer
import datetime
from address.models import Address, Locality, State, Country

pytestmark = pytest.mark.django_db


class TestOfferForm:
    def test_offer_form_clean(self):
        business = mixer.blend("business.Business")
        country = Country.objects.create(name="Kenya", code="KE")
        state = State.objects.create(name="Nairobi", country=country)
        locality = Locality.objects.create(name="USIU", state=state)
        address = Address.objects.create(
            street_number="USIU Road Thika road",
            locality=locality,
            raw="USIU road",
            latitude="-1.2211537",
            longitude="36.88339089999999",
        )
        form = forms.OfferForm(
            data={
                "code": "1234",
                "business": business.pk,
                "title": "Test offer",
                "start_date": datetime.datetime.now(),
                "limit": 4,
                "location": address.pk,
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
                "location": address.pk,
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
                "location": address.pk,
            }
        )
        instance = form2.save()
        assert instance.title == "Test offer"
