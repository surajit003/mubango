from django.shortcuts import HttpResponse
from .models import Business
import json


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
