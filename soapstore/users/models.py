import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name', 'email']

    def __str__(self):
        return self.phone_number

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, perm, obj=None):
       return self.is_staff

    @property
    def is_superuser(self):
        return self.is_staff

    def get_full_name(self):
        "Returns the full name for the user."
        return self.full_name

    def get_short_name(self):
        "Returns the short name for the user."
        return self.full_name