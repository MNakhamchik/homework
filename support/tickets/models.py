from django.db import models
import uuid
from django.contrib.auth.models import User
from users.models import Answer


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('Нерешенный', 'Нерешенный'),
        ('Решенный', 'Решенный'),
        ('Замороженный', 'Замороженный'),
    )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='new')  #
    answer = models.ManyToManyField(Answer)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title
