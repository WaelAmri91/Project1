from django.urls import path

from hub.models import Student
from.views import StudentCreateView, coachs_List, homePage, student_detail, studentCreate, studentCreateForm, students_List,StudentListView,add_student

urlpatterns = [
    path('home/', homePage, name="home"),
    path('index/',students_List, name="index"),
    path('index1/',coachs_List, name="index1"),
    path('index/<int:id>',student_detail, name="details"),
    path('listStudent', StudentListView.as_view(),name="eleve"),
    path('addStudent',studentCreate,name='Student_Create'),
    path('addStudent2',studentCreateForm,name='Student_Create2'),
    path('addStudent3',add_student,name='Student_Create3'),
    path('addStudent4',StudentCreateView.as_view(),name='Student_Create4')





    # path('student/<int:id>',student_details,name="details"),

]