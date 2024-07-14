from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
from datetime import datetime
from .utils import verify_token
from django.conf import settings
import jwt
from django.core.mail import EmailMessage
from accounts.models import CustomUser


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
            print("i'm in try")
            book = Book.objects.all()
            serialzier = BookSerializer(book, many = True)
            return JsonResponse({"success":True, "book":serialzier.data})   
        except Exception as e:
            print("im in error")
            print(e)
            return JsonResponse({"error":"error"})
        
    def post(self, request):
        try:
            token = request.query_params.get('token')
            if not token:
                return JsonResponse({"error": "Invalid token"})
            result = verify_token(token)
            if "error" in result and result["error"]:
                return JsonResponse({"error": result["error"]})
            
            if "success" in result and result["success"] == True:
                try:
                    decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
                    user_id = decoded_token["user_id"]
                    user = CustomUser.objects.get(id=user_id)
                    if not user.role == "admin" and not user.role == "librarian":
                        return JsonResponse({"error": "Only admin and librarian roles are allowed"})
                except Exception as e:
                    data = {"error": "User not found"}
                    return JsonResponse(data)
                data = json.loads(request.body)
                isbn = data.get('isbn')
                book_exists = False
                if check_value(isbn):
                    try:
                        book_obj = Book.objects.get(isbn=isbn)
                        if book_obj:
                            return JsonResponse({"error":"Book with this isbn already exists"})
                    except Book.DoesNotExist:
                        pass
                else:
                    return JsonResponse({"error":"ISBN number is Required"})
                title = data.get('title')
                author = data.get('author')
                publisher = data.get('publisher')
                year  = data.get('year')
                date_compos = year.split('-')
                year = datetime(int(date_compos[2]),int(date_compos[1]),int(date_compos[0])).strftime("%Y-%m-%d")
                genre = data.get('genre')
                quantity = data.get('quantity')
                new_arrival = data.get('new_arrival')
                trending = data.get('trending')
                available = data.get('available')
                if (check_value(isbn) and check_value(title) and check_value(author) and check_value(publisher) and check_value(year) and check_value(genre) and check_value(quantity)):
                    pass
                else:
                    return JsonResponse({"error":"Please provide all required fields"})
                
                book = Book.objects.create(isbn=isbn, title=title,author=author, publisher=publisher, year=year, genre=genre, quantity=quantity, available=available if available is not None else True, new_arrival=new_arrival if new_arrival is not None or not new_arrival == "" else False, trending= trending if trending is not None or not trending == "" else False)
                serializer = BookSerializer(book)
                email = EmailMessage(
                'New Books Arrival',
                'New Books Are Arrived Check it out',              
                settings.DEFAULT_FROM_EMAIL,
                ['uveshpathan665@gmail.com'],
                )
                email.attach()
                email.send()

                return JsonResponse({"success": True, "book": serializer.data})
            else:
                return JsonResponse({"error": False, "message": "Please login to Add book"})
        except Exception as e:
            return JsonResponse({"error":str(e)})
    
    def put(self,request):
        try:
            token = request.query_params.get('token')
            if not token:
                return JsonResponse({"error": "Invalid token"})
            result = verify_token(token)
            if "error" in result and result["error"]:
                return JsonResponse({"error": result["error"]})
            
            if "success" in result and result["success"] == True:
                try:
                    decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
                    user_id = decoded_token["user_id"]
                    user = CustomUser.objects.get(id=user_id)
                    if not user.role == "admin" and not user.role == "librarian":
                        return JsonResponse({"error": "Only admin and librarian roles are allowed"})
                except Exception as e:
                    data = {"error": "User not found"}
                    return JsonResponse(data)
                data = json.loads(request.body)
                isbn = data.get('isbn')
                try:
                    book = Book.objects.get(isbn=isbn)
                except Book.DoesNotExist:
                    return JsonResponse({"error":"Book not found"}) 
                title = data.get('title')
                author = data.get('author')
                publisher = data.get('publisher')
                new_arrival = data.get('new_arrival')
                trending = data.get('trending')
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
                if check_value(new_arrival):
                    book.new_arrival = new_arrival
                if check_value(trending):
                    book.trending = trending

                book.save()    
                serializer = BookSerializer(book)
                return JsonResponse({"success": True, "book": serializer.data, "message": "Book updated successfully"})
            else:
                return JsonResponse({"error": False, "message": "Please login to Update book"})
        except Exception as e:
            return JsonResponse({"error":str(e)})
    
    def delete(self, request):
        try:
            token = request.query_params.get('token')
            if not token:
                return JsonResponse({"error": "Invalid token"})
            result = verify_token(token)
            if "error" in result and result["error"]:
                return JsonResponse({"error": result["error"]})
            
            if "success" in result and result["success"] == True:
                try:
                    decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
                    user_id = decoded_token["user_id"]
                    user = CustomUser.objects.get(id=user_id)
                    if not user.role == "admin" and not user.role == "librarian":
                        return JsonResponse({"error": "Only admin and librarian roles are allowed"})
                except Exception as e:
                    data = {"error": "User not found"}
                    return JsonResponse(data)
                body = json.loads(request.body)
                isbn = body.get('isbn','')
                if check_value(isbn) == False:
                   return JsonResponse({"error": "ISBN number is required"}) 
                try:
                    book = Book.objects.get(isbn=isbn)
                    book.delete()
                    return JsonResponse({"success": True, "message": "Book deleted successfully"})
                except Book.DoesNotExist:
                    return JsonResponse({"error": "Book does not exist"})
            else:
                return JsonResponse({"error": False, "message": "Please login to Update book"})
        except Exception as e:
            return JsonResponse({"error":str(e)})


@api_view(["GET"])
def getBook(request, isbn=None):
    try:
        token = request.GET.get('token')
        if not token:
            return JsonResponse({"error": "Invalid token"})
        result = verify_token(token)
        if "error" in result and result["error"]:
            return JsonResponse({"error": result["error"]})
        
        if "success" in result and result["success"] == True:
            try:
                decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
                user_id = decoded_token["user_id"]
                user = CustomUser.objects.get(id=user_id)
            except Exception as e:
                data = {"error": "User not found"}
                return JsonResponse(data)
            if isbn is None:
                return JsonResponse({"error": "ISBN is required"})
            book = Book.objects.get(isbn=isbn)
            serializer = BookSerializer(book)
            return JsonResponse({"success": True, "book": serializer.data})
    except Exception as e:
        return JsonResponse({"error":str(e)})
    
@api_view(["POST"])
def borrowBook(request):
    try:
        token = request.GET.get('token')
        if not token:
            return JsonResponse({"error": "Invalid token"})
        result = verify_token(token)
        if "error" in result and result["error"]:
            return JsonResponse({"error": result["error"]})
        
        if "success" in result and result["success"] == True:
            try:
                decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
                user_id = decoded_token["user_id"]
                user = CustomUser.objects.get(id=user_id)
            except Exception as e:
                data = {"error": "User not found"}
                return JsonResponse(data)    
    except Exception as e:
        return JsonResponse({"error":str(e)})
