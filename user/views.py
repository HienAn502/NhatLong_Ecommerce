from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

from custom_admin.models import Product, Category


# Create your views here.


def index(request):
    return render(request, 'index.html')


def get_list_product(request):
    '''
        TODO:
            return list bao gồm tất cả các product
    '''
    products = Product.objects.all()
    get_list_product = []
    for product in products:
        get_list_product.append(product.to_dict())

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
def get_page_category(request, page=2, size=10 ):
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

def add_cart_item(request, product_id):
    '''
        TODO:
            Validate product_id tồn tại
            Tạo Cart Item với quantity default = 1
            Lưu Cart Item
    '''


def update_cart_item(request, product_id):
    '''
        TODO:
            Validate product_id tồn tại
            Cập nhật quantity product
            Nếu quantity <= 0 => Xóa khỏi database
    '''


def remove_from_cart(request, cart_item_id, cart_id):
    '''
        TODO:
            Validate cart_item_id, cart_id tồn tại
            Xóa cart_item khỏi database
    '''


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

