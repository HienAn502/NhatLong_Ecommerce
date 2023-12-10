import json
from unicodedata import category

from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from custom_admin.models import Product, Category


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


@csrf_exempt
def create_product(request):
    '''
    TODO:
        method: GET
            Render the Add Product page with the form
        method: POST
            Validate the information in the form
            Add a new product to the database and redirect to the page with all products
    '''
    if request.method=="POST":
        request_data= json.load(request.body.decode('utf-8'))
        name = request_data.get("name")
        description = request_data.get("description")
        try:
            quantity=int(request_data.get("quantity"))
            price = float(request_data.get("price"))
        except  TypeError as error:
            return HttpResponseBadRequest("bro, it must be a number")
        category_id = request_data.get("category_id")
        category = get_object_or_404(Category, id=category_id)

        image = request_data.get("imgURL")
        product = Product(name=name, description=description, quantity=quantity, price=price, category_id=category, imgURL=image)
        product.save()
        return JsonResponse(status=100, data=product.to_dict(), safe=False)
    elif request.method == "GET":
        return JsonResponse(status=200, data={"text": "product page"})
    else:
        return  HttpResponseNotAllowed('menthod not  allow')

@csrf_exempt
def create_category(request):
    pass
    if request.method == "POST":
        request_data = json.load(request.body.decode('utf-8'))
        name = request_data.get("name")
        description = request_data.get("description")

        category = Category(name=name, description=description)
        category.save()
        return JsonResponse(status=100, data=category.to_dict(), safe=False)

    elif request.method == "GET":
        return JsonResponse(status=200, data={"text": "category page"})
    else:
        return HttpResponseNotAllowed('menthod not  allow')





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
