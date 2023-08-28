from django.db import models
from django.urls import reverse

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    def url_delete(self):
        return reverse('delete', kwargs={'pk': self.pk})

    def url_update(self):
        return reverse('update', kwargs={'pk': self.pk})

