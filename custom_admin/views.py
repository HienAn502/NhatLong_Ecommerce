import json

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import logout as auth_logout

from custom_admin import authentication
from custom_admin.models import Product, Category, Order


@authentication()
def admin_dashboard(request):
    '''
    TODO:
        Render the custom_admin dashboard with relevant statistics and information
    '''
    total_products = Product.objects.count()
    total_orders = Order.objects.count()

    # Add more statistics or information as needed

    return render(request, 'admin_index.html', {'total_products': total_products, 'total_orders': total_orders})


def logout(request):
    auth_logout(request)
    return redirect('/')


def get_list_product(request):
    '''
        TODO:
            return list bao gồm tất cả các product
    '''
    products = Product.objects.all()
    get_list_product = [product.to_dict() for product in products]
    return JsonResponse(get_list_product, status=200, safe=False)


def get_list_category(request):
    products = Product.objects.all()
    get_list_category = []
    for product in products:
        get_list_category.append(product.to_dict())

    get_list_category = [product.to_dict() for product in products]
    return JsonResponse(get_list_category, status=200)


def get_page_product(request):
    '''
        TODO:
            return trang tất cả product nhưng bao gồm phân trang
            product.html
    '''
    page = request.GET.get('page', 1)
    size = request.GET.get('size', 50)

    # Convert page and size to integers
    page = int(page)
    size = int(size)
    products = Product.objects.all()
    paginator = Paginator(products, size)
    page_obj = paginator.get_page(page)
    response_data = {
        "total_elements": paginator.count,
        "total_pages": paginator.num_pages,
        "current_page": page,
        "content": [product.to_dict() for product in page_obj.object_list]
    }
    return render(request, 'products/list.html', context=response_data)


def get_page_category(request):
    page = request.GET.get('page', 1)
    size = request.GET.get('size', 50)

    # Convert page and size to integers
    page = int(page)
    size = int(size)
    categorys = Category.objects.all()
    paginator = Paginator(categorys, size)
    page_obj = paginator.get_page(page)
    response_data = {
        "total_elements": paginator.count,
        "total_pages": paginator.num_pages,
        "current_page": page,
        "content": [category.to_dict() for category in page_obj.object_list]
    }
    return render(request, 'categories/list.html', context=response_data)


def get_page_user(request):
    page = request.GET.get('page', 1)
    size = request.GET.get('size', 50)

    # Convert page and size to integers
    page = int(page)
    size = int(size)
    users = User.objects.all()
    paginator = Paginator(users, size)
    page_obj = paginator.get_page(page)
    users_dict = []
    for user in page_obj.object_list:
        users_dict.append({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": "ADMIN" if user.is_superuser else "USER",
            "date_joined": user.date_joined
        })
    response_data = {
        "total_elements": paginator.count,
        "total_pages": paginator.num_pages,
        "current_page": page,
        "content": users_dict
    }
    return render(request, 'users/list.html', context=response_data)


@csrf_exempt
@authentication()
def create_user(request):
    '''
    TODO:
        method: GET
            Render the Add User page with the form
        method: POST
            Validate the information in the form
            Add a new user to the database and redirect to the page with all users
    '''


@csrf_exempt
@authentication()
def create_product(request):
    '''
    TODO:
        method: GET
            Render the Add Product page with the form
        method: POST
            Validate the information in the form
            Add a new product to the database and redirect to the page with all products
    '''
    if request.method == "POST":
        # For file uploads, use request.FILES for the image field
        name = request.POST.get("name")
        description = request.POST.get("description")
        try:
            quantity = int(request.POST.get("quantity"))
            price = float(request.POST.get("price"))
        except TypeError as error:
            return JsonResponse({"error": "bro, it must be a number"}, status=400)

        category_id = request.POST.get("category_id")
        category = get_object_or_404(Category, id=category_id)

        # Handle file upload separately from other form fields
        image = request.FILES.get("img", None)

        product = Product(name=name, description=description, quantity_available=quantity, price=price, category_id=category,
                          imgUrl=image)
        product.save()

        # return redirect('custom_admin:admin_page_product')
        return JsonResponse({"status": "success", "data": product.to_dict()})
    elif request.method == "GET":
        categories = Category.objects.all()
        return render(request, 'products/add.html', {"categories": categories})
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def create_category(request):
    if request.method == "POST":
        request_data = json.loads(request.body.decode('utf-8'))
        name = request_data.get("name")
        description = request_data.get("description")

        category = Category(name=name, description=description)
        category.save()
        return JsonResponse(status=200, data=category.to_dict(), safe=False)

    elif request.method == "GET":
        return render(request, 'categories/add.html')
    else:
        return HttpResponseNotAllowed('menthod not  allow')


@authentication()
def edit_product(request, product_id):
    '''
    TODO:
        method: GET
            Render the Update Product page with the form
        method: POST
            Validate the information in the form
            Update the product information in the database and redirect to the page with all products
    '''
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        try:
            quantity = int(request.POST.get("quantity"))
            price = float(request.POST.get("price"))
        except TypeError as error:
            return JsonResponse({"error": "bro, it must be a number"}, status=400)

        category_id = request.POST.get("category_id")
        category = get_object_or_404(Category, id=category_id)

        # Handle file upload separately from other form fields
        image = request.FILES.get("img", None)

        product.name = name
        product.description = description
        product.quantity_available = quantity
        product.price = price
        product.category_id = category
        product.imgUrl = image
        product.save()
        # return redirect('custom_admin:admin_page_product')
        return JsonResponse({"status": "success", "data": product.to_dict()})
    elif request.method == "GET":
        categories = Category.objects.all()
        return render(request, 'products/edit.html', {"product": product, "categories": categories})
    elif request.method == "DELETE":
        try:
            # Delete the product
            product.delete()
            return HttpResponse("Product deleted successfully")
        except Product.DoesNotExist:
            return HttpResponse("Error: Product not found", status=404)
    else:
        return HttpResponseNotAllowed("Method Not Allowed")


@authentication()
def edit_user(request, user_id):
    '''
    TODO:
        method: GET
            Render the Update User page with the form
        method: POST
            Validate the information in the form
            Update the user information in the database and redirect to the page with all users
    '''


@authentication()
def order_list(request):
    '''
    TODO:
        Render a page with a list of all orders for custom_admin
    '''
    orders = Order.objects.all()

    return render(request, 'order_list.html', {'orders': orders})


@authentication()
def order_detail(request, order_id):
    '''
    TODO:
        Render a page with details of a specific order
    '''
    order = get_object_or_404(Order, id=order_id)

    return render(request, 'order_detail.html', {'order': order})


@authentication()
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


@authentication()
def edit_order(request, order_id):
    '''
    TODO:
        method: GET
            Render the Update Category page with the form
        method: POST
            Validate the information in the form
            Update the category information in the database and redirect to the page with all categories
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


def edit_category(request):
    return None