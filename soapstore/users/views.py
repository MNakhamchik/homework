from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from product.forms import OrderForm, UpdateCartItemForm
from .models import User
from product.models import Product, Cart, CartItem, Order
from .forms import RegistrationForm, LoginForm


def homepage(request): #главная страница
    return render(request, 'product/home.html')


# вход
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password2']
            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'register.html', {'form': form, 'error_message': 'Invalid login credentials'})
    else:
        form = LoginForm()

    return render(request, 'users/register.html', {'form': form})


def user_register(request):  # регистрации
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'users/register.html', {'form': form})


# отображения корзины
def view_cart(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart_items = CartItem.objects.filter(cart=cart)
    #расчет общей суммы
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'users/cart.html', context)


#оформление заказа
@login_required
def checkout(request):
    user = request.user
    cart = Cart.objects.get(user=user)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = user
            order.cart = cart
            order.save()

            for item in cart.items.all():
                order.items.add(item)

            # Удаление товаров из базы данных после оформления заказа
            cart.items.all().delete()

            return redirect('home')

    return render(request, 'checkout.html')


@login_required
#добавление в товара в корзину
def add_to_cart(request, id):
    # Получение объекта товара или возврат ошибки 404, если он не найден
    product = get_object_or_404(Product, id=id)

    # Получение объекта корзины пользователя или создание новой, если не существует
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Пытаемся найти CartItem с таким же продуктом, если он уже в корзине
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += 1  # Если товар уже в корзине, увеличиваем количество
        cart_item.save()
    except CartItem.DoesNotExist:
        # Если товара нет в корзине, создаем новый объект CartItem и добавляем его в корзину
        cart_item = CartItem.objects.create(cart=cart, product=product)

    return render(request, 'users/cart.html')


#очищение в корзины
def clear_cart(request):
    if request.method == 'POST':
        user = request.user
        cart_items = CartItem.objects.filter(user=user)

        # Очистка корзины
        cart_items.delete()

        messages.success(request, 'Корзина очищена успешно!')
        return redirect('cart')

    return render(request, 'clear_cart.html')


#удаление товаров
def remove_item_from_cart(request, pk):
    # Получаем текущего пользователя
    user = request.user
    cart = Cart.objects.get(user=user)
    item = get_object_or_404(CartItem, id=pk, cart=cart)
    price = item.product.price
    # Удаляем товар из корзины
    item.delete()
    # Обновляем общую стоимость корзины
    cart.total_price -= price
    cart.save()

    messages.success(request, 'Товар успешно удален из корзины.')
    return redirect('cart')


#изменение количества товаров
def update_cart_item(request, pk):
    user = request.user
    cart = Cart.objects.get(user=user)
    item = get_object_or_404(CartItem, id=pk, cart=cart)

    if request.method == 'POST':
        form = UpdateCartItemForm(request.POST)
        if form.is_valid():
            new_quantity = form.cleaned_data['quantity']
            old_quantity = item.quantity
            price_per_item = item.product.price

            # Обновляем количество товара в корзине
            item.quantity = new_quantity
            item.save()

            # Обновляем стоимость
            cart.total_price += (new_quantity - old_quantity) * price_per_item
            cart.save()

            return redirect('cart')

    return render(request, 'update_cart_item.html')


#выход
def user_logout(request):
    logout(request)
    return redirect('home')









