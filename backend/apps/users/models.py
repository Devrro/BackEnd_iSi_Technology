from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import *
from django.db import models

from apps.users.managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        db_table = "users"

    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )


class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    class Meta:
        db_table = "profile"
