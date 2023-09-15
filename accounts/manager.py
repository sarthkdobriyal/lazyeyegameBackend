from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError("The password must be set")
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 1)


        if extra_fields.get('role') != 1:
            raise ValueError('Superuser must have role of Global Admin')
        return self.create_user(email, password, **extra_fields)

    def create_staffuser(self,  email, password, **extra_fields):
        if not email:
            raise ValueError('The given username must be set')
        if not password:
            raise ValueError("The password must be set")
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', 2)
        # email = self.normalize_email('email')
        print(email)
        user = self.model(email=email, password=password , **extra_fields)
        user.set_password(password)
        user.save()
        #using=self._db
        return user

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email must be set")
        if not password:
            raise ValueError("The password must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault('role', 3)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def get_by_natural_key(self, username_):
        return self.get(username=username_)