from django.views.generic import ListView
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

class StudentListView(ListView):
        model=Student
        template_name="hub/index.html"
        paginate_by=1        

def student_detail(request,id):
    student =Student.objects.get(id=id)
    return render(
        request,
        'Hub/st_details.html',
        {
            'student':student,
        }
    )        
     
