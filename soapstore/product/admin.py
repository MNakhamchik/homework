from django.contrib import admin
from .models import Product, Category, Review, SubCategory, CartItem

admin.site.register(Product)
admin.site.register(Category)
# admin.site.register(PopularProduct)
# admin.site.register(WeeklyProduct)
admin.site.register(Review)
admin.site.register(SubCategory)
admin.site.register(CartItem)


# Marina - 1234567