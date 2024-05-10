from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models
from django.core.validators import RegexValidator



class AccountManager(BaseUserManager):
    def create_user(self, fullname, phonenumber, password=None, **extra_fields):
        if not fullname:
            raise ValueError('User must have a fullname')
        if not phonenumber:
            raise ValueError('User must have a phone number')

        user = self.model(fullname=fullname, phonenumber=phonenumber, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, fullname, phonenumber, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(fullname, phonenumber, password, **extra_fields)


class Teacher(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?\d{1,20}$',
        message='Phone number must start with + and must not contain more than 20 digits.'
    )

    fullname = models.CharField(max_length=100)
    phonenumber = models.CharField(
        validators=[phone_regex], max_length=21, unique=True
    )

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = ['fullname']

    objects = AccountManager()

    # Specify related_name for groups and user_permissions
    groups = models.ManyToManyField(Group, related_name='teachers')
    user_permissions = models.ManyToManyField(Permission, related_name='teachers')

    def __str__(self):
        return self.phonenumber
