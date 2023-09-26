from django.contrib import admin
from django.urls import re_path
from . import views
#import include
from django.urls import path, include


urlpatterns = [
    path('<str:game>/patient/<int:patientid>/gamespecs', views.editGameSpecs, name='edit-game-specs'),
    path('<str:game>/patient/<int:patientid>/gamedata', views.getGameData, name='get-game-data'),
    path('<str:game>/patient/<int:patientid>/gamedata/edit', views.editGameData, name='edit-game-data'),
]
