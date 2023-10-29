from django.contrib.auth.models import User
from django.db import models

from custom_admin.models import Product


# Create your models here.


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, null=True)
    total_price = models.FloatField(null=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)

    def to_dict(self):
        return {
            "id": self.id,
            "status": self.id,
            "total_price": self.total_price,
            "create_data": self.create_date,
            "user": self.user.to_dict()
        }


class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.FloatField(null=True)
    total_price = models.FloatField(null=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)

    def to_dict(self):
        return {
            "id": self.id,
            "quantity": self.quantity,
            "price": self.quantity,
            "total_price": self.total_price,
            "create_date": self.create_date,
            "product": self.product.to_dict(),
            "cart": self.cart.to_dict()
        }
