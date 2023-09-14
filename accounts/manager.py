from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    def create_superuser(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(username=username, password=password, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.is_doctor = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_staffuser(self,  username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(username=username, password=password , **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.is_doctor = True
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model( username=username, password=password, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.is_doctor = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username_):
        return self.get(username=username_)