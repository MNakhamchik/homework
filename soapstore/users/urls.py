from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('cart/', views.view_cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_to_cart/<uuid:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
    path('user/logout/', views.user_logout, name='user_logout'),
    path('update_cart_item/<uuid:pk>/', views.update_cart_item, name='update_cart_item'),
]
