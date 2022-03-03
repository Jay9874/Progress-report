from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("scores", views.scores, name="scores")
]