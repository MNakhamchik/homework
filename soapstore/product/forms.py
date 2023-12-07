from django import forms
from .models import Product, Order, Category, Review, SubCategory


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


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity', 'status']  # You can customize the fields as needed

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)


class UpdateCartItemForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)













# class WeeklyProductForm(forms.ModelForm):
#     class Meta:
#         model = WeeklyProduct
#         fields = ['product']
#
#
# class PopularProductForm(forms.ModelForm):
#     class Meta:
#         model = PopularProduct
#         fields = ['product']