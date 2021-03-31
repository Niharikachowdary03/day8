from django.urls import path
from london import views

urlpatterns=[
     path('',views.home),
     path('demo/',views.chk),
     path('nc/',views.home),
     path('lg/',views.login),
     path('reg/',views.regi),
] 