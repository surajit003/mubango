from Mubango.celery_app import celery_app as app
from account.models import Profile
from address.models import State, Locality, Country, Address
from django.contrib.auth.models import User


@app.task(name="update_user_profile")
def update_profile(user_id, phone_number, address, country, u_state):
    user = User.objects.get(id=user_id)
    profile, _ = Profile.objects.get_or_create(user=user)
    profile.phone_number = phone_number
    profile.slug = profile.profile_id
    try:
        country = Country.objects.get(name__icontains=country)
    except Country.DoesNotExist:
        country = Country.objects.create(name=country)
    try:
        state = State.objects.get(name=u_state, country=country)
    except State.DoesNotExist:
        state = State.objects.create(name=u_state, country=country)
    try:
        locality = Locality.objects.get(name=u_state, state=state)
    except Locality.DoesNotExist:
        locality = Locality.objects.create(name=u_state, state=state)
    try:
        address = Address.objects.get(raw=address, locality=locality)
    except Address.DoesNotExist:
        address = Address.objects.create(raw=address, locality=locality)
    profile.address = address
    profile.active = True
    profile.save()
