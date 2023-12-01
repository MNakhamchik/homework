from django.contrib import admin
from .models import User
from product.models import Order, Cart


admin.site.register(User)
admin.site.register(Order)
admin.site.register(Cart)