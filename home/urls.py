from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('detail',views.detail,name='detail'),
    path('login',views.loginUser,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('logged_user',views.logged_user,name='logged_user'),
    path('save_participant', views.save_participant, name='save_participant'),
    path('update_save_participant', views.update_save_participant, name='update_save_participant'),
]

