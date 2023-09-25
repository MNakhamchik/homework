from django.forms import ModelForm
from . models import Ticket
from users.models import Answer


class TicketForm(ModelForm):   #для создание и обновление
    class Meta:
        model = Ticket
        fields = ['title', 'description']
        labels = {'title': 'Название тикета',
                  'description': 'Описание тикета'}


class TicketResponseForm(ModelForm):#форму для ответа на тикеты
    class Meta:
        model = Answer
        fields = ['sender', 'content']


class TicketStatusForm(ModelForm):# изменение статуса
    class Meta:
        model = Ticket
        fields = ['status']
        labels = {'status': 'Статус тикета'}

