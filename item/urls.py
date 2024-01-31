from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('detail/<int:pk>', views.detail, name='detail'),
    path('items', views.items, name='items'),
    path('<int:pk>/opinion', views.opinion, name='opinion')
]