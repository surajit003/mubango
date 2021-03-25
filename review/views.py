from django.http import JsonResponse
from django.views.generic import ListView

from .models import Review
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
