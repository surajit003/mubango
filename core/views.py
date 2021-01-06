from django.shortcuts import render


# Create your views here.


def Index(request):
    if request.method == "GET":
        return render(request, "core/index.html")
