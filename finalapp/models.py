from django.db import models

class CategoryMaster(models.Model):
    categoryname = models.CharField(max_length=30)
    categorydescription = models.TextField()
    def __str__(self):
        return self.categoryname

