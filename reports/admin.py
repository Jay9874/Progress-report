from django.contrib import admin
# from matplotlib.pyplot import cla
from .models import Students, Reports
# from django.contrib.auth.models import  User
# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    pass
    list_display = ("first", "last")

class ReportsAdmin(admin.ModelAdmin):
    pass
    list_display = ("candidate", "semester", "Physics")



admin.site.register(Students, StudentsAdmin)
admin.site.register(Reports, ReportsAdmin)
admin.site.site_header = "Administrator Page"
admin.site.site_title = "Administrator Page"
admin.site.index_title = "Admin"