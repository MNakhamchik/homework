from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('create-product/', views.create_product, name='create_product'),
    path('delete-product/<int:pk>/', views.delete_product, name='delete_product'),
    path('products/<str:subcategory_id>/', views.product_list, name='product_list'),
    path('productsdetail/<str:id>/', views.product_detail, name='product_detail'),
    path('create-category/', views.create_category, name='create_category'),
    path('categories/', views.category_list, name='category_list'),
    path('category_detail/<uuid:category_id>/', views.category_detail, name='category_detail'),
    path('create-review/<int:pk>/', views.create_review, name='create_review'),
    path('products-of-the-week/', views.products_of_the_week, name='products_of_the_week'),
    path('popular-products/', views.popular_products, name='popular_products'),
]







