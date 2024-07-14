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
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from accounts.models import CustomUser
from .models import Book, Transaction
from .serializers import TransactionSerializer
from accounts.serializers import CustomUserSerializer
from django.core.mail import send_mail

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
            serialzier = BookSerializer(book, many = True)
            return JsonResponse({"success":True, "book":serialzier.data})   
        except Exception as e:
            return JsonResponse({"error":f"error : {str(e)}"})
        
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
                description = data.get('description')
                year  = data.get('year')
                # date_compos = year.split('-')
                # year = datetime(int(date_compos[2]),int(date_compos[1]),int(date_compos[0])).strftime("%Y-%m-%d")
                genre = data.get('genre')
                quantity = data.get('quantity')
                new_arrival = data.get('new_arrival')
                trending = data.get('trending')
                available = data.get('available')
                if (check_value(isbn) and check_value(title) and check_value(author) and check_value(publisher) and check_value(year) and check_value(genre) and check_value(quantity)):
                    pass
                else:
                    return JsonResponse({"error":"Please provide all required fields"})
                
                book = Book.objects.create(isbn=isbn,description=description, title=title,author=author, publisher=publisher, year=year, genre=genre, quantity=quantity, available=available if available is not None else True, new_arrival=new_arrival if new_arrival is True or new_arrival is False else False, trending= trending if trending is True or trending is False else False)
                serializer = BookSerializer(book)

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
def getBook(request):
    try:
        token = request.GET.get('token')
        isbn = request.GET.get('isbn')
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
        else:
            return JsonResponse({"error": False, "message": "Please login first"})
    except Exception as e:
        return JsonResponse({"error":str(e)})
    

@api_view(["GET"])
def GetAllBooksByUser(request):
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
            if not user:
                return JsonResponse({"error": "User not found"})
            transactions = Transaction.objects.filter(user=user)
            # Now, fetch all unique books related to these transactions
            related_books = Book.objects.filter(transaction__in=transactions).distinct()

            serializer = BookSerializer(related_books, many=True)
            return JsonResponse({"success": True, "books": serializer.data})
        else:
            return JsonResponse({"error": False, "message": "Please login first"})
    except Exception as e:
        return JsonResponse({"error":str(e)})
    

@api_view(['POST'])
def checkoutBook(request):
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
            if not user:
                return JsonResponse({"error": "User not found"})
            # Assuming request data includes user_id and book_id
            

            isbn = request.data.get('isbn')
            # full_name = request.data.get('full_name')
            # email = request.data.get('email')
            phone_number = request.data.get('phone_number')
            user.phone_number = phone_number
            # address = request.data.get('address')
            # city = request.data.get('city')
            # state = request.data.get('state')
            # pincode = request.data.get('pincode')
            quantity = request.data.get('quantity')

            if check_value(isbn) == False:
                return  JsonResponse({"error": "ISBN number is required"})
            # Retrieve user and book objects
            book = get_object_or_404(Book, isbn=isbn)

            # Check if the book is available
            if not book.available:
                return Response({'error': 'Book is not Available'}, status=status.HTTP_400_BAD_REQUEST)
            
            if (int(book.quantity) < int(quantity)):
                return Response({'error': f'Only {book.quantity} books available'}, status=status.HTTP_400_BAD_REQUEST)
            
            if book.quantity == 0:
                return Response({'error': f'Book is not available'}, status=status.HTTP_400_BAD_REQUEST)

            # Create a transaction record for checkout
            return_date = request.data.get('return_date')
            date_compos = return_date.split('-')
            return_date = datetime(int(date_compos[0]),int(date_compos[1]),int(date_compos[2])).strftime("%Y-%m-%d")
            transaction = Transaction(user=user, book=book, return_date=return_date,quantity=quantity, transaction_type='checkout')
            transaction.save()

            # Update book availability status
            book.quantity = int(book.quantity) - int(quantity)
            book.save()

            # Serialize and return transaction data
            serializer = TransactionSerializer(transaction)
            serialized_book = BookSerializer(book)
            serialized_user = CustomUserSerializer(user)
            return Response({"success":True, "book":serialized_book.data,"user":serialized_user.data, "transaction":serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({"error": False, "message": "Please login first"})
    except Exception as e:
        return JsonResponse({"error":str(e)})

@api_view(['POST'])
def returnBook(request):
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
            if not user:
                return JsonResponse({"error": "User not found"})
            # Assuming request data includes transaction_id
            transaction_id = request.data.get('transaction_id')

            # Retrieve transaction object
            try:
                transaction = Transaction.objects.get(id=transaction_id)
            except Transaction.DoesNotExist:
                return JsonResponse({"error": "Transaction does not exist"})


            # Ensure the book is checked out
            if transaction.transaction_type != 'checkout':
                return Response({'error': 'Transaction is not a checkout'}, status=status.HTTP_400_BAD_REQUEST)

            # Update transaction for return
            transaction.transaction_type = 'return'
            transaction.save()

            # Update book availability status
            book = transaction.book
            book.quantity = int(book.quantity) - int(transaction.quantity)
            book.save()
            html_message = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Overdue Book Return Reminder</title>
            </head>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
                    <div style="text-align: center; padding-bottom: 20px;">
                        <img src="your-logo-url" alt="Library Logo" style="max-width: 100px;">
                        <h1 style="margin: 0;">Public Library</h1>
                    </div>
                    <div style="padding: 20px;">
                        <p>Dear {user.full_name},</p>
                        <p>This is a friendly reminder that the book <strong>"{book.title}"</strong> you borrowed from our library is overdue for return.</p>
                        <p>If you have any questions or need assistance, feel free to contact us.</p>
                        <p>Thank you for your attention to this matter.</p>
                        <p>Best regards,</p>
                        <p><strong>Public Library</strong><br></p>
                    </div>
                    <div style="text-align: center; padding-top: 20px; font-size: 0.9em; color: #777;">
                        <p>&copy; 2024 Public Library. All rights reserved.</p>
                    </div>
                </div>
            </body>
            </html>


            """

            if transaction.is_overdue():
                send_mail(subject="Book is overdue",
                          from_email=settings.DEFAULT_FROM_EMAIL,
                          recipient_list=[user.email],
                          html_message=html_message)

            # Serialize and return updated transaction data
            serializer = TransactionSerializer(transaction)
            serialized_book = BookSerializer(book)
            serialized_user = CustomUserSerializer(user)
            return Response({"success":True, "book":serialized_book.data,"user":serialized_user.data, "transaction":serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({"error": False, "message": "Please login first"})            
    except Exception as e:
        return Response({"error": str(e)})
