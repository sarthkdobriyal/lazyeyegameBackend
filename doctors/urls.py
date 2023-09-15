from django.contrib import admin
from django.urls import re_path
from . import views
#import include
from django.urls import path, include


urlpatterns = [

    re_path('patients', views.getPatients),
    path('patient/<int:id>', views.editPatient, name='edit-patient'),

]
