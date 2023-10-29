from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "create_date": self.create_date
        }


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    price = models.FloatField(null=True)
    quantity_available = models.PositiveIntegerField(null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    imgUrl = models.ImageField(
        upload_to='blog/static/assets/img', blank=True, default='post-landscape-1.jpg')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "quantity_available": self.quantity_available,
            "category": self.category_id.to_dict(),
            "create_date": self.create_date,
            "imgUrl": self.imgUrl.url if self.imgUrl else ''
        }


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    total_price = models.FloatField(null=True)
    status = models.CharField(max_length=50, null=True)
    shipping_address = models.TextField(null=True)

    def update_total_price(self, new_price):
        self.total_price = new_price


    def to_dict(self):
        return {
            "id": self.id,
            "shipping_address": self.shipping_address,
            "status": self.status,
            "total_price": self.total_price,
            "create_date": self.create_date,
            "user": self.user.to_dict()
        }


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.FloatField(null=True)
    total_price = models.FloatField(null=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)

    def to_dict(self):
        return {
            "id": self.id,
            "quantity": self.quantity,
            "price": self.price,
            "total_price": self.total_price,
            "create_date": self.create_date,
            "product": self.product.to_dict(),
            "order": self.order.to_dict()
        }
