from django.db import models

# Create your models here.

class Dummy_model(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name