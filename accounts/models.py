from uuid import uuid4

from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.core.validators import RegexValidator
from django.utils import timezone


from django.db import models

from .manager import AccountManager


# Create your models here.
USERNAME_PATTERN = '^[a-z0-9+]{2,25}$'
USERNAME_ERROR_MESSAGE = 'invalid username format'


class Account(AbstractBaseUser, PermissionsMixin):

    # These fields tie to the roles!
    ADMIN = 1
    STAFF = 2
    USER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (STAFF, 'Doctor'),
        (USER, 'Patient'),
    )
    

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'



    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=25, unique=True, validators=[
                                RegexValidator(regex=USERNAME_PATTERN, message=USERNAME_ERROR_MESSAGE)])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    created_date = models.DateTimeField(default=timezone.now)
    email = models.EmailField(max_length=50, unique=True)
    category = models.TextField(null=True, blank=True)
    contactno = models.CharField(max_length=10, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    mrdnumber = models.CharField(max_length=50, null=True, blank=True)
    modified_date = models.DateTimeField(default=timezone.now)

    # tenant = models.ForeignKey('tenant.Tenant', on_delete=models.CASCADE, null=True, blank=False)

    REQUIRED_FIELDS = ['email', 'password']
    USERNAME_FIELD = 'username'

    objects = AccountManager()


class DoctorPatientRelationship(models.Model):
    doctor = models.ForeignKey(Account, related_name='patients', on_delete=models.CASCADE)
    patient = models.ForeignKey(Account, related_name='doctors', on_delete=models.CASCADE)