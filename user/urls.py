from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("product/list/", views.get_list_product)
]
