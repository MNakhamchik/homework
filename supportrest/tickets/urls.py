from django.urls import path
from .views import TicketList,TicketDetail,TicketResponse,CreateTicket,ChangeTicketStatus


urlpatterns = [
    path('tickets/', TicketList.as_view(), name='tickets'),
    path('tickets/<int:pk>/', TicketDetail.as_view(), name='tickets-detail'),
    path('response-ticket/<int:pk>/', TicketResponse.as_view(), name='create-ticket'),
    path('create-ticket/', CreateTicket.as_view(), name='create-ticket'),
    path('ticket-status/<int:pk>/', ChangeTicketStatus.as_view(), name='ticket-status'),
]
