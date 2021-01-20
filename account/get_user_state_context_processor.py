from .models import Profile


def get_user_state(request):
    if request.user and not request.user.is_anonymous:
        try:
            profile = Profile.objects.get(user=request.user)
            return {"user_state": profile.get_state()}
        except Profile.DoesNotExist:
            return {"user_state": "Nairobi"}  # default location
    else:
        return {"user_state": "Nairobi"}  # default location
