from django.views.generic import ListView, DetailView

from offer.models import Offer, OfferSocial, OfferImage


class OfferListByRegion(ListView):
    model = Offer
    template_name = "offer/offer_search_by_region.html"
    paginate_by = 16

    def get_queryset(self):
        qs = Offer.offer_manager.top_five_offer_based_on_user_state(
            self.kwargs.get("region")
        )
        return qs


class OfferDetailView(DetailView):
    model = Offer
    template_name = "offer/offer_detail.html"

    def get_context_data(self, **kwargs):
        context = super(OfferDetailView, self).get_context_data(**kwargs)
        context["offer_social"] = OfferSocial.objects.filter(
            offer__slug=self.kwargs.get("slug"), active=True
        )
        context["gallery"] = OfferImage.objects.filter(
            offer__slug=self.kwargs.get("slug"), img_category="other"
        )
        context["slideshow"] = OfferImage.objects.filter(
            offer__slug=self.kwargs.get("slug"), img_category="top_slideshow"
        )
        return context


class OfferListView(ListView):
    paginate_by = 16
    model = Offer
    template_name = "offer/offer_featured_list.html"

    def get_context_data(self, **kwargs):
        context = super(OfferListView, self).get_context_data(**kwargs)
        offer_list = Offer.offer_manager.upcoming_offers(self.kwargs.get("state"))
        context["offer_list"] = offer_list
        return context
