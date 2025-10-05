from django.db import models

# Create your models here.
''' 
    
'''
class Item(models.Model):
    name = models.CharField(max_length=255)
    sell_in = models.IntegerField()
    quality = models.IntegerField()

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
