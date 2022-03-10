from ast import Sub
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from matplotlib.style import context
from pandas import read_sql_query
from sklearn import model_selection
from .models import Subjects, Student, Score 
# from .models import Student, Score




def student_home(request):
    student = Student.objects.get(admin=request.user.id)
    student_obj = Student.objects.get(admin=request.user.id)
    total_subjects = Subjects.objects.filter(student_id=student.id)

    subject_name = []

    context = {
        "total_subjects": total_subjects, 
        "subject_name": subject_name,
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "reports/home.html"
    )


def scores(request):
    student = Student.objects.get(admin=request.user.id)
    student_result = Score.objects.filter(student_id=student.id)

    context = {
        "student_result": student_result,
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "reports/scores.html", context)


def home(request):
    student = Student.objects.get(admin=request.user.id)

    context = {
        "student": student,
    }
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "reports/home.html")


def analytics(request):
    student = Student.objects.get(admin=request.user.id)
    student_result = Score.objects.filter(student_id=student.id)
    context = {
        "student_result": student_result,
    }
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "reports/analytics.html", context)
