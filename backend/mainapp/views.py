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
        return JsonResponse({"success":True})

    def post(self,request):
        try:
            data = json.loads(request.body)
            isbn = data.get('isbn')
            title = data.get('title')
            author = data.get('author')
            publisher = data.get('publisher')
            year  = data.get('year')
            date_compos = year.split('-')
            print(date_compos)
            year = datetime(int(date_compos[1]),int(date_compos[0]),int(date_compos[2])).strftime("%Y-%m-%d")
            genre = data.get('genre')
            quantity = data.get('quantity')
            available = data.get('available')
            if (check_value(isbn) and check_value(title) and check_value(author) and check_value(publisher) and check_value(year) and check_value(genre) and check_value(quantity)):
                pass
            else:
                return JsonResponse({"error":"Please provide all required fields"})
            
            book = Book.objects.create(isbn=isbn, title=title, publisher=publisher, year=year, genre=genre, quantity=quantity, available=available)
            serializer = BookSerializer(book, many=True)
            return JsonResponse({"success":True, "book":serializer})
        except Exception as e:
            return JsonResponse({"error":str(e)})
    

    def put(self,request):
        return JsonResponse({"success":"I am in put"})
    
    def delete(self, request):
        print("Id is:")
        body = json.loads(request.body)
        id = body.get('id')
        print("Id is:",id)
        return JsonResponse({"success":"I am in delete"})


