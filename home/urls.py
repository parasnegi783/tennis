from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('save_participant/', views.save_participant, name='save_participant'),
    path('save_event1/',views.save_event1,name='save_event1'),
    path('save_event2/',views.save_event2,name='save_event2'),
]

