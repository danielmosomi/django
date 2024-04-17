from django.urls import path
from.import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('About us/', views.register, name='About us'),
    path('myregister/', views.myregister, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addregister', views.addregister, name='addregister'),
]