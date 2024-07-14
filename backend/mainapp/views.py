from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import JsonResponse

# Create your views here.
class Books(generics.RetrieveUpdateDestroyAPIView):
    
    def add_book(self,request):
        if request.method == 'POST':
            isbn = request.POST.get('isbn')
            title = request.POST.get('title')
            authoer = request.POST.get('authoer')
            publisher = request.POST.get('publisher')
            year  = request.POST.get('year')
            genre = request.POST.get('genre')
            quantity = request.POST.get('quantity')
            avialable = request.POST.get('avialable')

    def get_books(self,request):
            book = Book.objects.all()
            serializer = BookSerializer   

            if serializer.is_valid():
                 serializer.save()
            return JsonResponse(serializer.data)   

    def update_book(self,request):
        pass

    def delete_book(self,request):
        pass