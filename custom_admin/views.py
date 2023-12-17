import json
from unicodedata import category

from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.views.decorators.csrf import csrf_exempt

from custom_admin.models import Product, Category, Order


def admin_dashboard(request):
    '''
    TODO:
        Render the custom_admin dashboard with relevant statistics and information
    '''
    total_products = Product.objects.count()
    total_orders = Order.objects.count()

    # Add more statistics or information as needed

    return render(request, 'admin_dashboard.html', {'total_products': total_products, 'total_orders': total_orders})


def product_list(request):
    '''
    TODO:
        Render a page with a list of all products for custom_admin
    '''

    def product_list(request):
        # Assuming you have a Product model with appropriate fields
        products = Product.objects.all()

        return render(request, 'product_list.html', {'products': products})


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

    def edit_product(request, product_id):
        # Assuming you have a Product model and a corresponding ProductForm
        product = Product.objects.get(id=product_id)

        if request.method == 'POST':
            form = Product(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return render('all_products')  # Redirect to the page with all products
        else:
            form = Product(instance=product)

        return render(request, 'edit_product.html', {'form': form, 'product': product})



    pass


def delete_product(request, product_id):
    '''
    TODO:
        If product_id exists - Delete the product from the database
        If not - return an error message
    '''


    # Assuming you have a Product model in your database
    try:
        # Try to get the product with the given product_id
        product = Product.objects.get(id=product_id)
        # Delete the product
        product.delete()
        return HttpResponse("Product deleted successfully")
    except Product.DoesNotExist:
        # If the product with the given product_id doesn't exist
        return HttpResponse("Error: Product not found", status=404)



def order_list(request):
    '''
    TODO:
        Render a page with a list of all orders for custom_admin
    '''
    orders = Order.objects.all()

    return render(request, 'order_list.html', {'orders': orders})


def order_detail(request, order_id):
    '''
    TODO:
        Render a page with details of a specific order
    '''
    order = get_object_or_404(Order, id=order_id)

    return render(request, 'order_detail.html', {'order': order})


def update_order_status(request, order_id):
    '''
    TODO:
        method: GET
            Render the Update Order Status page with the form
        method: POST
            Validate the information in the form
            Update the order status in the database and redirect to the page with all orders
    '''
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        form = Order(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('all_orders')  # Redirect to the page with all orders
    else:
        form = Order(instance=order)

    return render(request, 'update_order_status.html', {'form': form, 'order': order})
