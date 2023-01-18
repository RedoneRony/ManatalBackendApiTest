from django.urls import path,include
from schoolApp.views import schoolAppViews as views

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


router = routers.DefaultRouter()

router.register("schools", views.SchoolsViewSet, basename='School')
router.register("students", views.StudentViewSet, basename='Student')


school_router = routers.NestedDefaultRouter(router, "schools", lookup="school")
school_router.register("students", views.SchoolsStudentsViewSet, basename="school-students")
student_router = routers.NestedDefaultRouter(router, "students", lookup="Student")


urlpatterns = [
    path("", include(router.urls)),
    path("", include(school_router.urls)),
    path("students/", include(student_router.urls))
]
