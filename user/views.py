from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect

from custom_admin.models import Product, Category
from user import authentication
from user.forms import CustomUserCreationForm
from user.models import ShoppingCart, CartItem


# Create your views here.


def index(request):
    categories = Category.objects.all()
    data = {
        "items": [],
        "categories": categories
    }
    for category in categories:
        data['items'].append({
            "category_id": category.id,
            "category_name": category.name,
            "products": Product.objects.filter(category_id=category)
        })
    return render(request, 'index.html', data)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            auth_login(request, user)

            return redirect('user:index')
        else:
            messages.error(request, f"{form.error_messages}")
    else:
        form = CustomUserCreationForm()

    return render(request, 'authentication/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                # Redirect to a success page or home page
                return redirect('user:index')  # Replace 'home' with the URL name of your home page
        else:
            messages.error(request, f"{form.error_messages}")
    else:
        form = AuthenticationForm()

    return render(request, 'authentication/login.html', {'form': form})


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


def get_page_product(request, page=1, size=10):
    '''
        TODO:
            return trang tất cả product nhưng bao gồm phân trang
            product.html

    '''
    products = Product.objects.all()
    paginator = Paginator(products, size)
    page_obj = paginator.get_page(page)
    response_data = {
        "total_elements": paginator.count,
        "total_pages": paginator.num_pages,
        "current_page": page,
        "content": [product.to_dict() for product in page_obj.object_list]
    }
    return JsonResponse(response_data, status=200)


def get_page_category(request, page=2, size=10):
    categorys = Category.objects.all()
    paginator = Paginator(categorys, size)
    page_obj = paginator.get_page(page)
    response_data = {
        "total_elements": paginator.count,
        "total_pages": paginator.num_pages,
        "current_page": page,
        "content": [category.to_dict() for category in page_obj.object_list]
    }
    return JsonResponse(response_data, status=200)


def get_product(request, product_id):
    '''
        TODO:
            return product với product_id tương ứng
    '''


@authentication()
def add_cart_item(request, product_id):
    '''
        TODO:
            Validate product_id tồn tại
            Tạo Cart Item với quantity default = 1
            Lưu Cart Item
     '''
    product = add_cart_item(Product, id=product_id)
    user_cart, created = ShoppingCart.objects.get_or_create(user=request.user)

    # Check if the product is already in the cart
    if product in user_cart.products.all():
        # Update quantity or perform any other action
        pass
    else:
        # Add the product to the cart
        user_cart.products.add(product)


def update_cart_item(request, product_id):
    '''
        TODO:
            Validate product_id tồn tại
            Cập nhật quantity product
            Nếu quantity <= 0 => Xóa khỏi database
    '''
    product = update_cart_item(Product, id=product_id)
    user_cart, created = ShoppingCart.objects.get_or_create(user=request.user)

    # Check if the product is in the cart
    if product in user_cart.products.all():
        # Perform the update logic based on your requirements
        # For example, updating quantity or removing the item
        # For simplicity, let's assume you want to double the quantity
        cart_item = user_cart.cart_items.get(product=product)
        cart_item.quantity *= 2
        cart_item.save()


def remove_from_cart(request, cart_item_id, cart_id):
    '''
        TODO:
            Validate cart_item_id, cart_id tồn tại
            Xóa cart_it em khỏi database
    '''
    user_cart = remove_from_cart(ShoppingCart, id=cart_item_id, user=request.user)
    cart_item = remove_from_cart(CartItem, id=cart_item_id, cart=user_cart)

    # Remove the item from the cart
    cart_item.delete()


def create_order(request):
    '''
        TODO:
        * Làm sau *
            Tạo Order từ user_id, address
            Lấy order_id
            Tạo các OrderItem với order_id và product_list
            Tính total_price của Order
            Cập nhật total_price của Order
    '''


def get_order_detail(request, order_id):
    '''
        TODO:
            Trả về thông tin order, và list order item
    '''

def error(request):
    code = request.GET.get('code', 500)
    message = request.GET.get('message', "Something went wrong")
    return render(request, 'error.html', {"code": code, "message": message})