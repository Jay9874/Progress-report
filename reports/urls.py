from django.urls import path
from . import views
# from django.conf import settings
from django.conf.urls.static import static

app_name = "reports"

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("analytics", views.analytics, name="analytics"),
    path("scores", views.scores, name="scores")
]