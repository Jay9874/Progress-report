from django.urls import path

from reports import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "reports"

urlpatterns = [
    path("", views.student_home, name="student_home"),
    path("analytics", views.analytics, name="analytics"),
    path("scores", views.scores, name="scores")
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)

