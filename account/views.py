from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# Create your views here.
def login(request):
    return render(request, "account/login.html")


def home(request):
    return render(request, "account/home.html")
