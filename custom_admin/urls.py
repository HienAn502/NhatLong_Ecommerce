from django.urls import path
from . import views

app_name = "custom_admin"
urlpatterns = [
    path("", views.admin_dashboard, name='admin_dashboard'),
    path("product/page/", views.get_page_product, name='admin_page_product'),
    path("category/page/", views.get_page_category, name='admin_page_category'),
    path("product/<int:product_id>", views.edit_product, name="edit_product"),

    path("logout/", views.logout, name='logout'),

]
