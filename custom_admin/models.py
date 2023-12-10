from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    quantity_available = models.PositiveIntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    imgUrl = models.ImageField(
        upload_to='blog/static/assets/img', blank=True, default='post-landscape-1.jpg')

    def to_dict(self):
        '''
        Convert Product instance to a dictionary.
        '''
        product_dict = {}
        # Get all fields of the Product model
        fields = [field.name for field in self._meta.get_fields()]

        for field in fields:
            # Exclude internal fields starting with _
            if not field.startswith('_'):
                product_dict[field] = getattr(self, field)

                # If it's a ManyToManyField, convert related objects to a list of dictionaries
                if isinstance(product_dict[field], models.Manager):
                    product_dict[field] = [item.to_dict() for item in product_dict[field].all()]

        return product_dict


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    status = models.CharField(max_length=50)
    shipping_address = models.TextField()


    def update_total_price(self, new_price):
        self.total_price = new_price


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    total_price = models.FloatField()
