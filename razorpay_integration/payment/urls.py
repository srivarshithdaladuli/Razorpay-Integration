from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_order/', views.create_order, name='create_order'),
]
