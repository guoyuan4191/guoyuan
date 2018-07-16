from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=32,unique=True)
    pub_date = models.DateField()
    publish = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return self.title
