from django.shortcuts import HttpResponse
from .models import Business
import json


# Create your views here.


def search_for_business(request, city):
    if request.method == "GET":
        response = [
            obj.as_dict() for obj in Business.business_manager.closest_clubs(city)
        ]
        return HttpResponse(
            json.dumps({"data": response}), content_type="application/json"
        )
