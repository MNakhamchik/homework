from django import forms
from .models import Product, Order, Category, Review, SubCategory, Cart, CartItem


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'photo', 'description', 'price', 'weight', 'country', 'brand', 'rating']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name_subcategory', 'category']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'text', 'rating']


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['products']


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'address', 'phone']


class UpdateCartItemForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)


