from django.shortcuts import render
from business.models import Business
from event.models import Event
from account.models import Profile
from account.context_processor import get_user_state_and_profile_id


# Create your views here.


def Index(request):
    if request.method == "GET":
        if not request.user.is_anonymous:
            profile = Profile.objects.get(user=request.user)
            clubs_featured = Business.business_manager.six_closest_clubs(
                profile.get_state()
            )
            club_currently_hot_list = Business.business_manager.currently_hot_clubs(
                profile.get_state()
            )
            event_featured_list = Event.event_manager.upcoming_events(
                profile.get_state()
            )
            return render(
                request,
                "core/index.html",
                {
                    "clubs_featured": clubs_featured,
                    "club_currently_hot_list": club_currently_hot_list,
                    "event_featured_list": event_featured_list,
                    "club_list_six_header": "Featured Clubs in your Area",
                },
            )
        else:
            state = get_user_state_and_profile_id(request)
            clubs_featured = Business.business_manager.six_closest_clubs(
                state["user_state"]
            )
            club_currently_hot_list = Business.business_manager.currently_hot_clubs(
                state["user_state"]
            )
            event_featured_list = Event.event_manager.upcoming_events(
                state["user_state"]
            )

            return render(
                request,
                "core/index.html",
                {
                    "clubs_featured": clubs_featured,
                    "club_currently_hot_list": club_currently_hot_list,
                    "event_featured_list": event_featured_list,
                    "club_list_six_header": "Featured Clubs in {}".format(
                        state["user_state"]
                    ),
                },
            )
