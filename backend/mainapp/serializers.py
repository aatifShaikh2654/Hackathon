from rest_framework import serializers
from .models import Book


# Here Define all your model serializers
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"