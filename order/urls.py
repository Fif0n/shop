from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('submit/', views.sumbit, name='submit'),
    path('history/', views.history, name='history')
]