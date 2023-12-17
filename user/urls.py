from django.urls import path
from . import views
from .views import register, login

urlpatterns = [
    path("", views.index),
    path("product/list/", views.get_list_product),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("error/", views.error, name='error')
]
