from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import ListView, UpdateView, DeleteView

from account.models import Profile
from .models import Review, BusinessServiceRating, Service
from business.models import Business


def save_review(request):
    if request.method == "POST" and request.is_ajax():
        print("req", request.POST, request.FILES)
        image1 = request.FILES.get("image_1")
        image2 = request.FILES.get("image_2")
        image3 = request.FILES.get("image_3")
        print("im", image1, image2, image3)
        comment = request.POST.get("comment")
        experience = request.POST.get("experience")
        user = request.user
        b_slug = request.POST.get("business_slug")
        business = Business.objects.get(slug=b_slug)
        Review.objects.create(
            business=business,
            user=user,
            comment=comment,
            experience=experience,
            image_1=image1,
            image_2=image2,
            image_3=image3,
        )
        data = {"status": 201, "response": "Review Saved Successfully"}
        return JsonResponse(data, safe=False)


def add_service_rating(request):
    if request.method == "POST" and request.is_ajax():
        user = request.user
        b_slug = request.POST.get("business_slug")
        business = Business.objects.get(slug=b_slug)
        service_name = request.POST.get("service_name")
        rating = int(request.POST.get("rating"))
        service, _ = Service.objects.get_or_create(name=service_name)
        business_service_rating, _ = BusinessServiceRating.objects.get_or_create(
            business=business,
            user=user,
            service=service,
        )
        business_service_rating.rating = rating
        business_service_rating.save()
        data = {"status": 200, "response": "Review Saved Successfully"}
        return JsonResponse(data, safe=False)


class ReviewList(ListView):
    model = Review
    template_name = "review/user_review_list.html"
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super(ReviewList, self).get_context_data(**kwargs)
        context["profile"] = Profile.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class ReviewUpdate(UpdateView):
    model = Review
    template_name = "review/update_review.html"
    paginate_by = 10
    fields = (
        "comment",
        "experience",
        "user",
        "business",
    )

    def form_valid(self, form):
        review = form.save(commit=False)
        business = Business.objects.get(slug=form.cleaned_data.get("business"))
        review.business = business
        review.save()

    def get_context_data(self, *args, **kwargs):
        context = super(ReviewUpdate, self).get_context_data(**kwargs)
        context["profile"] = Profile.objects.get(user=self.request.user)
        return context

    def get_success_url(self):
        return redirect("review:user_review_list")

    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only authors can update stories """
        obj = self.get_object()
        print("entered")
        if obj.user != self.request.user:
            print("entered here")
            return redirect("review:user_review_list")
        return super(ReviewUpdate, self).dispatch(request, *args, **kwargs)


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = "review/review_confirm_delete.html"
    success_url = "/mb/review/all/"

    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only authors can update stories """
        obj = self.get_object()
        if obj.user != self.request.user:
            return redirect("review:user_review_list")
        return super(ReviewDeleteView, self).dispatch(request, *args, **kwargs)
