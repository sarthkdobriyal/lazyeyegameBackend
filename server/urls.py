from django.contrib import admin
from django.urls import re_path
from . import views
#import include
from django.urls import path, include


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
    re_path('doctor/',include('doctors.urls')),
    re_path('game/',include('games.urls')),
]
