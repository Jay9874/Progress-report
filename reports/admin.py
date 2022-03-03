from django.contrib import admin
from matplotlib.pyplot import cla
from .models import Students, Reports
# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    list_display = ("first", "last")

class ReportsAdmin(admin.ModelAdmin):
    list_display = ("candidate", "year")



admin.site.register(Students, StudentsAdmin)
admin.site.register(Reports, ReportsAdmin)