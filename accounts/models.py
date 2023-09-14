from uuid import uuid4

from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.core.validators import RegexValidator
from django.utils import timezone


from django.db import models

from .manager import AccountManager


# Create your models here.
USERNAME_PATTERN = '^[a-z0-9+]{2,25}$'
USERNAME_ERROR_MESSAGE = 'invalid username format'


class Account(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=25, unique=True, validators=[
                                RegexValidator(regex=USERNAME_PATTERN, message=USERNAME_ERROR_MESSAGE)])
    is_active = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    email = models.EmailField(max_length=50, unique=True)
    # tenant = models.ForeignKey('tenant.Tenant', on_delete=models.CASCADE, null=True, blank=False)

    REQUIRED_FIELDS = ['email', 'password']
    USERNAME_FIELD = 'username'

    objects = AccountManager()