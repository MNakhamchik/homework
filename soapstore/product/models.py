import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from users.models import User


class Category(models.Model): #категория товаров, с иерархией
    category = models.CharField(max_length=255)
    category_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.category


class SubCategory(models.Model):  #подкатегория товаров
    name_subcategory = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name_subcategory


class Product(models.Model):   #товар
    name = models.CharField(max_length=100)  #поле имени товара.
    photo = models.ImageField(upload_to='product_photos', blank=True)  #изображение
    description = models.TextField()# описания товара
    weight = models.DecimalField(max_digits=6, decimal_places=2)#вес товара
    price = models.DecimalField(max_digits=8, decimal_places=2)#цены товара
    country = models.CharField(max_length=100)#страна производителя товара
    brand = models.CharField(max_length=100) #бренд товара
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products')
    is_product_of_the_week = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name


class Review(models.Model): #отзывы
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_reviews')
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reviews')  # пользователь, который оставил отзыв
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


class Cart(models.Model):  # корзина
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"Cart for {self.user.username}"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())


class CartItem(models.Model): #конкретные товары добавленные в карзину
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='cart_items', null=True)  # пользователь, который оставил отзыв

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.product.name} in {self.cart.user.username}'s cart"


class Order(models.Model):  # заказ
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    cart_item = models.ManyToManyField(CartItem)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'Order {self.id}'