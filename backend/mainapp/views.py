from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
from datetime import datetime


def check_value(value):
    print("Value is", value)
    if value is None or value == "":
        return False
    else:
        return True

# Create your views here.
class Books(generics.RetrieveUpdateDestroyAPIView):    
    def get(self, request):
        try:
            book = Book.objects.all()
            serialzier = BookSerializer(book)
            return JsonResponse({"success":True}, serialzier.data,safe=False)   
        except Exception as e:
            print(e)
            return JsonResponse({"error":"error"})
    def post(self, request):
        try:
            data = json.loads(request.body)
            isbn = data.get('isbn')
            title = data.get('title')
            author = data.get('author')
            publisher = data.get('publisher')
            year  = data.get('year')
            date_compos = year.split('-')
            year = datetime(int(date_compos[2]),int(date_compos[1]),int(date_compos[0])).strftime("%Y-%m-%d")
            genre = data.get('genre')
            quantity = data.get('quantity')
            available = data.get('available')
            if (check_value(isbn) and check_value(title) and check_value(author) and check_value(publisher) and check_value(year) and check_value(genre) and check_value(quantity)):
                pass
            else:
                return JsonResponse({"error":"Please provide all required fields"})
            
            book = Book.objects.create(isbn=isbn, title=title,author=author, publisher=publisher, year=year, genre=genre, quantity=quantity, available=available if available is not None else True)
            serializer = BookSerializer(book)
            return JsonResponse({"success": True, "book": serializer.data})
        except Exception as e:
            return JsonResponse({"error":str(e)})
    

    def put(self,request):
        try:
            data = json.loads(request.body)
            isbn = data.get('isbn')
            try:
                book = Book.objects.get(isbn=isbn)
            except Book.DoesNotExist:
                return JsonResponse({"error":"Book not found"}) 
            title = data.get('title')
            author = data.get('author')
            publisher = data.get('publisher')
            year  = data.get('year')
            date_compos = year.split('-')
            if check_value(year):
                year = datetime(int(date_compos[2]),int(date_compos[1]),int(date_compos[0])).strftime("%Y-%m-%d")
            genre = data.get('genre')
            quantity = data.get('quantity')
            available = data.get('available')
            if check_value(title):
                book.title = title
            if check_value(author):
                book.author = author
            if check_value(publisher):
                book.publisher = publisher
            if check_value(year):
                book.year = year
            if check_value(genre):
                book.genre = genre
            if check_value(available):
                book.available = available

            book.save()    
            serializer = BookSerializer(book)
            return JsonResponse({"success": True, "book": serializer.data, "message": "Book updated successfully"})
        except Exception as e:
            return JsonResponse({"error":str(e)})
    
    def delete(self, request):
        body = json.loads(request.body)
        id = body.get('id')
        return JsonResponse({"success":"I am in delete"})


