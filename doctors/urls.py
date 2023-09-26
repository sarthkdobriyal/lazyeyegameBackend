from django.contrib import admin
from django.urls import re_path
from . import views
#import include
from django.urls import path, include


urlpatterns = [

    re_path('patients', views.getPatients),
    path('patient/<int:id>', views.getPatient, name='patient'),
    path('patient/<int:id>/edit', views.editPatient, name='edit-patient'),
    path('patient/<int:id>/delete', views.deletePatient, name='delete-patient'),
    path('patient/<int:id>/toggle-active', views.togglePatientActive, name='toggle-patient-active'),

]
