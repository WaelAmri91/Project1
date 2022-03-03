from re import template
from django.views.generic import ListView,CreateView
from django.shortcuts import render,redirect
from django.http import HttpResponse
from hub.forms import StudentForm, StudentModelForm

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
        #paginate_by=1        

def student_detail(request,id):
    student =Student.objects.get(id=id)
    return render(
        request,
        'Hub/st_details.html',
        {
            'student':student,
        }
    )        

def studentCreate (request):
    print(request)
    if request.method =='POST':
        first_Name=request.POST.get('first_name')   
        last_Name=request.POST.get('last_name')  
        email=request.POST.get('email')
        Student.objects.create(
            first_name = first_Name,
            last_name = last_Name,
            email = email
        )
        return redirect('eleve')
    return render (
        request,
        'hub/add_student.html'
    )    
def studentCreateForm(request):
    form = StudentForm()
    if request.method =='POST' :
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(
                first_name = form.cleaned_data.get('first_name'),
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email']
            )
            #Student.objects.create(**form.cleaned_data)
    return render(
        request,
        'hub/add_student.html',
        {
            'form':form 
        }
    )
def add_student (request) :
    form = StudentModelForm()
    if request.method =='POST':
        form=StudentModelForm(request.POST)
        if form.is_valid():
            student=form.save(commit=False)
            # traitement
            student.save()
            return redirect('eleve')
    return render(
            request,
            'hub/add_student.html',
            {
                'form': form
            }
        )    
class StudentCreateView(CreateView):
      model = Student
      form_class = StudentModelForm
      template_name="hub/add_student.html"
    


      
     
