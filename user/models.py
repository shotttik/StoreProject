from django.core.validators import validate_email
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

from user.location_choices import Location
from user.status_choices import Status


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        validate_email(email)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self,  email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('mobile_phone', 0)
        extra_fields.setdefault('personal_number', 0)
        extra_fields.setdefault('member_status', 1)
        extra_fields.setdefault('location', 1)
        extra_fields.setdefault('balance', 0)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='E-Mail', unique=True)
    personal_number = models.CharField(verbose_name='პირადი ნომერი', unique=True, max_length=11)
    mobile_phone = models.CharField(verbose_name='ტელეფონის ნომერი', max_length=9)
    member_status = models.PositiveSmallIntegerField(choices=Status.choices, blank=True, null=True)
    location = models.PositiveSmallIntegerField(choices=Location.choices)
    address = models.CharField(verbose_name='მისამართი', max_length=255)
    balance = models.DecimalField(verbose_name="ბალანსი", max_digits=8, decimal_places=2, default=0,
                                  help_text="$")
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
