from django.urls import path
from . import views

urlpatterns = [
    path('', views.tickets, name='tickets'),
    path('ticket/<str:pk>/', views.ticket, name='ticket'),
    path('create-ticket/', views.create_ticket, name='create-ticket'),
    path('ticket-list/', views.ticket_list, name='ticket-list'),
    path('ticket-detail/<str:pk>', views.ticket_detail, name='ticket-detail'),
    path('respond/<str:pk>', views.respond_to_ticket, name='respond'),
    path('change-status/<str:pk>', views.change_ticket_status, name='change-status'),

]
