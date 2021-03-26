from django.shortcuts import HttpResponse, render
from .models import Business, BusinessSocial
from review.models import BusinessServiceRating, Review
import json
from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin


# Create your views here.


def get_all_business(request, state):
    if request.method == "GET":
        response = [
            obj.as_dict() for obj in Business.business_manager.closest_clubs(state)
        ]
        return HttpResponse(
            json.dumps({"data": response}), content_type="application/json"
        )


def search_for_a_specific_business(request, name, state):
    if request.method == "GET":
        response = [
            obj.as_dict()
            for obj in Business.business_manager.get_specific_business(name, state)
        ]
        return HttpResponse(
            json.dumps({"data": response}), content_type="application/json"
        )


class ClubListView(ListView):
    paginate_by = 16
    model = Business
    template_name = "business/clubs/clubs_list_all.html"

    def get_context_data(self, **kwargs):
        context = super(ClubListView, self).get_context_data(**kwargs)
        context["club_list"] = Business.business_manager.closest_clubs(
            self.kwargs.get("state")
        )
        return context


class ClubDetailView(MultipleObjectMixin, DetailView):
    model = Business
    template_name = "business/clubs/club_detail.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        object_list = Review.objects.filter(business__slug=self.kwargs.get("slug"))
        context = super(ClubDetailView, self).get_context_data(
            object_list=object_list, **kwargs
        )
        context["review_count"] = Review.objects.filter(
            business__slug=self.kwargs.get("slug")
        ).count()
        amenities = BusinessServiceRating.objects.filter(
            business__slug=self.kwargs.get("slug")
        ).select_related("service")

        context["business_social"] = BusinessSocial.objects.filter(
            business__slug=self.kwargs.get("slug"), active=True
        )
        context["club_amenities"] = amenities
        return context


class ClubListByRegion(ListView):
    model = Business
    template_name = "business/clubs/club_search_by_region.html"
    paginate_by = 16

    def get_queryset(self):
        qs = Business.business_manager.closest_clubs(self.kwargs.get("region"))
        return qs
