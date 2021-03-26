from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView

from .models import Profile
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from .tasks import update_profile
from datetime import timedelta
from django.utils.timezone import now


def validate_username(request):
    username = request.GET.get("username", None)
    data = {"is_taken": User.objects.filter(username__iexact=username).exists()}
    return JsonResponse(data)


def validate_phonenumber(request):
    phone_number = request.GET.get("phonenumber", None)
    data = {"is_taken": Profile.objects.filter(phone_number=phone_number).exists()}
    return JsonResponse(data)


def validate_email(request):
    email = request.GET.get("email", None)
    data = {"is_taken": User.objects.filter(email__iexact=email).exists()}
    return JsonResponse(data)


def Home(request):
    return render(request, "account/home.html")


def LogoutView(request):
    logout(request)
    return redirect("core:home")


def LoginView(request):
    if request.method == "POST" and request.is_ajax():
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return JsonResponse(
                    {"status": 200, "response": "Login Successful"}, safe=False
                )
        else:
            return JsonResponse(
                {"status": 401, "response": "Username or Password is Incorrect"},
                safe=False,
            )


def SignupView(request):
    if request.method == "POST" and request.is_ajax():
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        phone_number = request.POST["phone_number"]
        address = request.POST["address"]
        country = request.POST["country"]
        u_state = request.POST["state"]
        user = User.objects.create(
            username=username, email=email, first_name=first_name, last_name=last_name
        )
        user.set_password(password)
        user.is_active = True
        user.save()
        # update_profile.apply_async(
        #     [user.id, phone_number, address, country, u_state],
        #     eta=now() + timedelta(seconds=3),
        # )
        update_profile(user.id, phone_number, address, country, u_state)

        # adding a small delay or else the task is unable to access the user record simultaneously
        if user:
            if user.is_active:
                login(
                    request, user, backend="django.contrib.auth.backends.ModelBackend"
                )
                return JsonResponse(
                    {"status": 201, "response": "Registration Successful"}, safe=False
                )
        else:
            return JsonResponse(
                {
                    "status": 200,
                    "response": "Registration Not Successful. Please try again",
                },
                safe=False,
            )


class ProfileDetail(DetailView):
    model = Profile
    template_name = "account/profile.html"


def UpdateProfile(request, slug):
    if request.method == "POST" and request.is_ajax():
        profile_image = request.FILES.get("profile_image")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone_number")
        profile = Profile.objects.get(profile_id=slug)
        profile.user.first_name = first_name
        profile.user.last_name = last_name
        profile.user.email = email
        profile.phone_number = phone
        profile.image = profile_image
        profile.user.save()
        profile.save()
        data = {"status": 204, "response": "Profile Updated Successfully"}
        return JsonResponse(data, safe=False)


def UpdatePassword(request, slug):
    if request.method == "POST" and request.is_ajax():
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        profile = Profile.objects.get(profile_id=slug)
        valid = profile.user.check_password(current_password)
        if valid:
            profile.user.set_password(new_password)
            profile.user.save()
            data = {"status": 204, "response": "Password Update Successfull"}
            return JsonResponse(data, safe=False)
        else:
            data = {"status": 200, "response": "Current Password is Incorrect"}
            return JsonResponse(data, safe=False)
