from typing import List
from django.shortcuts import render
from django.http import HttpResponse

from hub.models import Coach, Student

# Create your views here.
def homePage(request):
    return HttpResponse("<h1>Welcome to the ...</h1>")
def students_List(request):
    list =Student.objects.all()
    return render(
        request,
        'Hub/index.html',
        {
            'students':list,
        }
    )    
def coachs_List(request):
    list =Coach.objects.all()
    return render(
        request,
        'Hub/index1.html',
        {
            'coachs':list,
        }
    )        
def student_detail(request,id):
    student =Student.objects.get(id=id)
    return render(
        request,
        'Hub/st_details.html',
        {
            'student':student,
        }
    )        
     
