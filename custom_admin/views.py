from django.shortcuts import render

from custom_admin.models import Product


def admin_dashboard(request):
    '''
    TODO:
        Render the custom_admin dashboard with relevant statistics and information
    '''
    pass


def product_list(request):
    '''
    TODO:
        Render a page with a list of all products for custom_admin
    '''
    pass


def create_product(request):
    '''
    TODO:
        method: GET
            Render the Add Product page with the form
        method: POST
            Validate the information in the form
            Add a new product to the database and redirect to the page with all products
    '''
    pass


def edit_product(request, product_id):
    '''
    TODO:
        method: GET
            Render the Update Product page with the form
        method: POST
            Validate the information in the form
            Update the product information in the database and redirect to the page with all products
    '''
    pass


def delete_product(request, product_id):
    '''
    TODO:
        If product_id exists - Delete the product from the database
        If not - return an error message
    '''
    pass


def order_list(request):
    '''
    TODO:
        Render a page with a list of all orders for custom_admin
    '''
    pass


def order_detail(request, order_id):
    '''
    TODO:
        Render a page with details of a specific order
    '''
    pass


def update_order_status(request, order_id):
    '''
    TODO:
        method: GET
            Render the Update Order Status page with the form
        method: POST
            Validate the information in the form
            Update the order status in the database and redirect to the page with all orders
    '''
    pass
