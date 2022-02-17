from django.urls import path

from hub.models import Student
from.views import coachs_List, homePage, student_detail, students_List

urlpatterns = [
    path('home/', homePage, name="home"),
    path('index/',students_List, name="index"),
    path('index1/',coachs_List, name="index1"),
    path('index/<int:id>',student_detail, name="details"),

]