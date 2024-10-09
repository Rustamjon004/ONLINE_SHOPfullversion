from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('detail/<int:product_id>/', views.product_detail, name='detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/change-quantity/<int:cart_product_id>/<str:action>/', views.change_cart_product_quantity, name='change_cart_product_quantity'),

]