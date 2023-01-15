from django.urls import path,include
from schoolApp.views import schoolAppViews as views

urlpatterns = [
    path('createSchool/',
         views.createSchool, name="create-school"),
    path('schools/', views.getSchoolsInfo,
         name="get-school-info"),
    path('schools/<str:pk>/', views.getSchoolById,
     name="get-school-info-byId"),
    path('updateSchool/<str:pk>/', views.updateSchoolInfo, name="school-info-update"),
    path('deleteSchool/<str:pk>/', views.deleteSchool, name="school-delete"),

    path('createStudent/',
         views.createStudent, name="create-student"),
    path('students/', views.getStudentInfo,
         name="get-student-info"),
    path('students/<str:pk>/', views.getStudentById,
     name="get-student-info-byId"),
    path('updateStudent/<str:pk>/', views.updateStudentInfo, name="student-info-update"),
    path('deleteStudent/<str:pk>/', views.deleteStudent, name="student-delete"),
]
