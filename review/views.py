from django.http import JsonResponse
from django.views.generic import ListView

from .models import Review
from business.models import Business


def save_review(request):
    if request.method == "POST" and request.is_ajax():
        comment = request.POST.get("comment")
        experience = request.POST.get("experience")
        user = request.user
        b_slug = request.POST.get("business_slug")
        business = Business.objects.get(slug=b_slug)
        Review.objects.create(
            business=business, user=user, comment=comment, experience=experience
        )
        data = {"status": 201, "response": "Review Saved Successfully"}
        return JsonResponse(data, safe=False)
