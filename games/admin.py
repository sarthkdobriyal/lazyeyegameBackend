from django.contrib import admin
from .models import PacmanData,RollexData,TetrisData
# Register your models here.
admin.site.register(PacmanData)
admin.site.register(RollexData)
admin.site.register(TetrisData)