from django.contrib import admin
from django.urls import re_path
from . import views
#import include
from django.urls import path, include


urlpatterns = [
    path('game/<str:game>/patient/<int:patientid>', views.editGame, name='edit-game'),
]
