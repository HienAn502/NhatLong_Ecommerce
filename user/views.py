from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'index.html')


def get_list_product(request):
    '''
        TODO:
            return list bao gồm tất cả các product
    '''


def get_page_product(request, page=1, size=10):
    '''
        TODO:
            return trang tất cả product nhưng bao gồm phân trang
            product.html
    '''


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

