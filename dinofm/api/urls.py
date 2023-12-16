from django.urls import path

from . import views

urlpatterns = [
    path('add_book', views.add_name, name='add_book'),
    path('get_name', views.get_name, name='get_name'),
]