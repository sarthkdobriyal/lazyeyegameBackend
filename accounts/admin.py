from django.contrib import admin
from .models import Account,DoctorPatientRelationship

# Register your models here.
admin.site.site_header = "Admin Panel"

admin.site.register(Account)
admin.site.register(DoctorPatientRelationship)