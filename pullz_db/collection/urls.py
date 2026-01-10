from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pulls/', views.pull_list, name='pull_list'),
    path('directory/', views.directory, name='directory'),
]