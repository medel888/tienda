from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_view, name='cart'),  
    path('agg/<int:product_id>,<int:qty>', views.cart_agg, name='cart_agg'), 
]