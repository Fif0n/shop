from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('<int:item_pk>/add', views.add, name='add'),
    path('<int:pk>/remove', views.remove, name='remove'),
    path('<int:pk>/change_quantity', views.change_quantity, name='change_quantity')
]