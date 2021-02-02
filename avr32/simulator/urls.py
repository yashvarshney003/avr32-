from django.contrib import admin
from django.urls import path,include
from simulator import views


urlpatterns = [
   
    path('',views.index,name= 'home'),
    path('assembler',views.assembler,name= 'assembler')
]