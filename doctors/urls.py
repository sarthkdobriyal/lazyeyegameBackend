from django.contrib import admin
from django.urls import re_path
from . import views
#import include
from django.urls import path, include


urlpatterns = [

    re_path('patients', views.getPatients),
    path('patient/<int:id>', views.editPatient, name='edit-patient'),
    path('patient/<int:id>', views.deletePatient, name='delete-patient'),
    path('patient/<int:id>/toggle-active', views.togglePatientActive, name='toggle-patient-active'),

]
