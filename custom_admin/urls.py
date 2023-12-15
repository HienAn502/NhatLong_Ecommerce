from django.urls import path
from  . import views
app_name = "custom_admin"
urlpatterns = [
    path("product/", views.create_product),
    path("category/", views.create_category)

]