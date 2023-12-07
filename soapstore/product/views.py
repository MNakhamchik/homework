from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, CategoryForm, ReviewForm
from .models import Product, Category, Review


def homepage(request): #главная страница
    return render(request, 'product/home.html')


@login_required
def create_product(request):    #создание товара
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, 'product/create_product.html', context)


@login_required
def delete_product(request, pk):   #удаление товаров
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('product_list')


def product_list(request):      #список всех товаров
    products = Product.objects.all()  # Получаем все объекты модели Product

    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):  #детальную информацию о выбранном товаре
    product = get_object_or_404(Product, id=pk)
    context = {'product': product}

    return render(request, 'product_detail.html', context)


@login_required
def create_category(request):  #создания и заполнения категорий.
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # Перенаправление на страницу списка категорий
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})


def category_list(request):     #списка всех категорий
    categories = Category.objects.all()
    return render(request, 'product/catalog.html', {'categories': categories})


def category_detail(request, category_id):   #детальную информацию о выбранной категории и все товары в этой категории
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'category_detail.html', context)


@login_required
def create_review(request, pk):     # отзывы к товарам
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('product_detail', product_id=pk)
    else:
        form = ReviewForm()

    return render(request, 'create_review.html', {'form': form, 'product': product})


def add_review(request, pk):
    product = Product.objects.get(id=pk)
    user = request.user
    rating = request.POST.get('rating')
    comment = request.POST.get('comment')

    # Создаем отзыв
    review = Review.objects.create(product=product, user=user, rating=rating, comment=comment)

    # Обновляем средний рейтинг товара
    product.average_rating = product.reviews.aggregate(Avg('rating'))['rating__avg'] or 0.0
    product.save()


def products_of_the_week(request):  #товаров недели
    products = Product.objects.filter(is_product_of_the_week=True).first()
    context = {
        'products': products
    }

    return render(request, 'your_app/week_products.html', context)


def popular_products(request):   #популярных товаров
    # Находим популярные товары, сортируя их по количеству заказов в убывающем порядке
    popular_products = Product.objects.annotate(num_orders=Count('order')).order_by('-num_orders')[:5]

    context = {
        'popular_products': popular_products
    }

    return render(request, 'products/popular.html', context)


