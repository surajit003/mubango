from django.shortcuts import render
from business.models import Business
from account.models import Profile

# Create your views here.


def Index(request):
    if request.method == "GET":
        profile = Profile.objects.get(user=request.user)
        clubs_featured = Business.business_manager.six_closest_clubs(
            profile.get_state()
        )
        club_currently_hot_list = Business.business_manager.currently_hot_clubs(
            profile.get_state()
        )
        return render(
            request,
            "core/index.html",
            {
                "clubs_featured": clubs_featured,
                "club_currently_hot_list": club_currently_hot_list,
            },
        )
