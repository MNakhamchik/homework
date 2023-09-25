from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from users.models import Profile, Answer
from .forms import TicketForm, TicketResponseForm, TicketStatusForm


@login_required
def tickets(request): #обрабатывает запрос пользователя на страницу с тикетами
    user_profile = Profile.objects.get(user=request.user)      #получаем профиль пользователя, через request.user
    if user_profile.role == 'support':  #проверяем , является ли суппортом, если да ,то извлекаем все тикеты из базы данных
        tickets = Ticket.objects.all()
    else:
        tickets = Ticket.objects.filter(owner=user_profile.user)  #если user, то извлекаем тикеты, которые принадлежат user
    return render(request, 'tickets/tickets.html', {'tickets': tickets})


@login_required
def ticket(request, pk): #отображение информации о конкретном тикете
    ticket = get_object_or_404(Ticket, id=pk) #получаем тикет по id, если нет, то ошибка 404
    user_profile = get_object_or_404(Profile, user=request.user) #профиль авторизированного пользователя, если нет, то ошибка 404
    answer = Answer.objects.filter(ticket=ticket) #запрос к бд, чтобы получить ответы тикета,
    context = {
        'ticket': ticket,
        'answer': answer
    }
    if user_profile.role == 'support':    #проверяем , является ли суппортом, если да ,то извлекаем все тикеты из базы данных
        return render(request, 'tickets/support-ticket.html', context)
    else:
        return render(request, 'tickets/user-ticket.html', context)  #если user, то извлекаем тикеты, которые принадлежат user


@login_required
def create_ticket(request):
    if request.user.is_authenticated:  # Проверяем, что пользователь авторизован
        if request.method == 'POST':
            form = TicketForm(request.POST)  #создаем экземпляр формы
            if form.is_valid():  #проверяем на валидацию
                ticket = form.save()
                return redirect('ticket_detail', id=ticket.pk)#если все ок, то ticket_detail все тикеты
        else:
            form = TicketForm()

        return render(request, 'create_ticket.html', {'form': form})#если что-то не так , то create_ticket создание тикета
    else:
        return HttpResponse("Вы должны быть авторизованы для создания тикета.")



@login_required
def ticket_list(request):#список тикетов
    tickets = Ticket.objects.all()
    return render(request, 'ticket_list.html', {'tickets': tickets})


@login_required
def ticket_detail(request, pk):#детали тикета по id
    ticket = get_object_or_404(Ticket, id=pk)
    return render(request, 'ticket_detail.html', {'ticket': ticket})


@login_required
def respond_to_ticket(request, pk): #обрабатывает запросы для создания и сохранения ответов
    ticket = get_object_or_404(Ticket, id=pk)

    if request.method == 'POST':
        form = TicketResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.ticket = ticket
            response.save()
            return redirect('ticket_detail', id=pk)
    else:
        form = TicketResponseForm()

    return render(request, 'answer_ticket.html', {'form': form, 'ticket': ticket})


@login_required
def change_ticket_status(request, pk): # изменение статуса тикета
    ticket = get_object_or_404(Ticket, id=pk)

    if request.method == 'POST':
        form = TicketStatusForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_detail', id=pk)
    else:
        form = TicketStatusForm(instance=ticket)

    return render(request, 'change_ticket_status.html', {'form': form, 'ticket': ticket})