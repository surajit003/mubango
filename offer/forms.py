from .models import Offer, UserOffer
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
        cleaned_data = self.cleaned_data
        code = cleaned_data.get("code")
        business = cleaned_data.get("business")
        if "business" in self.changed_data:
            print("etered")
            offer_code = Offer.objects.filter(code=code, business=business).exists()
            if offer_code:
                raise forms.ValidationError(
                    "A code exists for another offer for this business"
                )
        elif "code" in self.changed_data:
            offer_code = Offer.objects.filter(code=code, business=business).exists()
            if offer_code:
                raise forms.ValidationError(
                    "A code exists for another offer for this business"
                )
        else:
            return self.cleaned_data


class UserOfferForm(forms.ModelForm):
    class Meta:
        model = UserOffer
        fields = "__all__"
