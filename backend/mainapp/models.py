from django.db import models
from accounts.models import CustomUser
from datetime import timezone
# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=50,unique=True)
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
    

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    checkout_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.book.title} ({self.user.full_name})'

    def is_overdue(self):
        if self.return_date and self.return_date < timezone.now().date():
            return True
        return False