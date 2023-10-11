from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from .models import Ticket, Answer
from users.models import User
from .serializers import TicketSerializer, TicketResponseSerializer, TicketStatusSerializer
from .permissions import IsSupportUserOrOwnerTicket


class TicketList(generics.ListAPIView):#обрабатывает запрос пользователя на страницу с тикетами
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsSupportUserOrOwnerTicket]

    def get_queryset(self):
        user_profile = User.objects.get(user=self.request.user)
        if user_profile.role == 'support':
            return Ticket.objects.all()
        else:
            return Ticket.objects.filter(owner=user_profile.user)


class TicketDetail(generics.RetrieveAPIView):#детальное отображение информации , доступное только для аутентифицированных пользователей
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsSupportUserOrOwnerTicket]


class CreateTicket(generics.CreateAPIView):   #создание билетов
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsSupportUserOrOwnerTicket]


class TicketResponse(generics.CreateAPIView):  #создание ответов
    queryset = Answer.objects.all()
    serializer_class = TicketResponseSerializer
    permission_classes = [IsSupportUserOrOwnerTicket]

    def perform_create(self, serializer):
        ticket = get_object_or_404(Ticket, pk=self.kwargs.get('pk'))
        serializer.save(ticket=ticket)


class ChangeTicketStatus(generics.RetrieveUpdateAPIView):    # изменение статуса тикета
    queryset = Ticket.objects.all()
    serializer_class = TicketStatusSerializer
    permission_classes = [IsSupportUserOrOwnerTicket]
