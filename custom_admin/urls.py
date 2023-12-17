from django.urls import path
from . import views

app_name = "custom_admin"
urlpatterns = [
    path("", views.admin_dashboard, name='admin_dashboard'),

    path("product/", views.create_product, name='create_product'),
    path("product/page/", views.get_page_product, name='admin_page_product'),
    path("product/<int:product_id>/", views.edit_product, name='edit_product'),

    path("category/", views.create_category, name='create_category'),
    path("category/page/", views.get_page_category, name='admin_page_category'),
    path("category/<int:category_id>/", views.edit_category, name='edit_category'),

    path("user/", views.create_user, name='create_user'),
    path("user/page/", views.get_page_user, name='admin_page_user'),
    path("user/<int:user_id>/", views.edit_user, name='edit_user'),

    path("logout/", views.logout, name='logout'),

]
