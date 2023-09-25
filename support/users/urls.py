from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('register/', views.register, name='register'),

]