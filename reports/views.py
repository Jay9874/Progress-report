from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# from reports.models import Reports

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "reports/home.html")

def scores(request):
    # scores = Reports.objects.all()
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    return render(request, "reports/scores.html", {
        "scores": scores,

    })

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "reports/home.html")

def analytics(request):
    # students
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "reports/analytics.html")