from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    year = models.DateField()
    genre = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    trending = models.BooleanField(default=False)
    new_arrival = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)