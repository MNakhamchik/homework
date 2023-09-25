from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id_profile = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['created']


class Answer(models.Model):  #ответы
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.sender

    class Meta:
        ordering = ['-created']
