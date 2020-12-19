from .models import Offer
from django import forms


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = "__all__"

    def clean(self):
        """
        Override the default clean method to check whether this offer exists
        for a company.
        """
        print("entttttttt")
        cleaned_data = self.cleaned_data
        print("s", cleaned_data)
        code = cleaned_data.get("code")
        business = cleaned_data.get("business")
        print("code", code, business)
        offer_code = Offer.objects.filter(code=code, business=business).exists()
        print("offer", offer_code)
        if offer_code:
            raise forms.ValidationError(
                "A code exists for another offer for this business"
            )
        else:
            return self.cleaned_data
