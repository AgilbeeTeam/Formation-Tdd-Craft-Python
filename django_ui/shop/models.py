from django.db import models

# Create your models here.
''' 
    les items
'''
class Item(models.Model):
    name = models.CharField(max_length=255)
    sell_in = models.IntegerField()
    quality = models.IntegerField()

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(max_length=20, choices=[("PAID","Payée"),("PENDING","En attente")])
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name="cart")

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
