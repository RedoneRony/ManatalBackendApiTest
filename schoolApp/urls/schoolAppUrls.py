from django.urls import path,include
from schoolApp.views import schoolAppViews as views

urlpatterns = [
    path('',views.home, name="home"),

]
