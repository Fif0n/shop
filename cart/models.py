from django.db import models
from django.contrib.auth.models import User
from item.models import Item

class UserCart(models.Model):
    item = models.ForeignKey(Item, related_name='items', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def total_sum(items):
        sum = 0

        for item in items:
            sum += (item.item.price * item.quantity)
        
        return sum

