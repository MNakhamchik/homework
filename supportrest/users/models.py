from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager
import uuid


class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('support', 'Support')
    )

    users = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='subscriber')
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id_profile = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return str(self.username)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Answer(models.Model):  #ответы
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.sender

    class Meta:
        ordering = ['-created']
