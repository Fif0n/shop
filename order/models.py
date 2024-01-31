from django.db import models

from django.contrib.auth.models import User
from item.models import Item

STATUS = {
    0: 'Zamówienie złożone',
    1: 'Zamówienie wysłane',
}

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def total_sum(items):
        sum = 0

        for item in items:
            sum += (item.price * item.quantity)
        
        return sum

class OrderItem(models.Model):
    price = models.FloatField()
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, related_name='order_item', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='item', on_delete=models.CASCADE)

class OrderUserData(models.Model):
    order = models.ForeignKey(Order, related_name='order_data', on_delete=models.CASCADE)
    description = models.TextField()
    address = models.TextField()
    name = models.CharField(max_length=255)

