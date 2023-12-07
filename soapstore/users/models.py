import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)   #активен ли пользователь
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name', 'email', 'phone_number']

    def __str__(self):
        return self.phone_number














































# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):  #создание нового пользователя
#         if not email:
#             raise ValueError('The Email field must be set')
#
#         email = self.normalize_email(email)
#         username = self.model(email=email, **extra_fields)
#         username.set_password(password)
#         username.save(using=self._db)
#
#         return username
#
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         return self.create_user(email, password, **extra_fields)
#
#
# class User(AbstractBaseUser):
#     email = models.EmailField(max_length=255, unique=True)
#     full_name = models.CharField(max_length=30)
#     is_active = models.BooleanField(default=True)  #является ли аккаунт пользователя активным.
#     is_staff = models.BooleanField(default=False)   #имеет ли пользователь право входить в админ-панель Django.
#     is_superuser = models.BooleanField(default=False)  # имеет ли пользователь все разрешения без явного назначения.
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['full_name']
#
#     def get_full_name(self):
#         return f'{self.full_name}'
#
#     def get_short_name(self):
#         return self.full_name
#
#     def has_perm(self, perm, obj=None):
#         return self.is_superuser
#
#     def has_module_perms(self, app_label):
#         return self.is_superuser