from django.urls import path
from . import views
from .views import register, login

app_name = "user"
urlpatterns = [
    path("", views.index, name='index'),
    path("product/list/", views.get_list_product, name='product_list'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("error/", views.error, name='error')
]
