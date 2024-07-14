from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json 
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser, Address
from django.contrib.auth import authenticate
import requests
import jwt
from django.conf import settings
from django.core import serializers

# BASE URL FOR of backend
BASE_URL = "http://127.0.0.1:8000/"
# TODO: Forgot password
# TODO: Reset password

# Verify the token and return true if valid else return false
def verify_token(token):
    try:
        if not token:
            return JsonResponse({"error":"Token is required"})
        url = BASE_URL + "api/token/verify/"
        headers = {"Authorization": f"Bearer {token}"}
        body = {"token":token}
        result = requests.post(url, headers=headers, data=body)
        print(result)
        if result.status_code == 200:
            return {"success":True}
        else:
            return {"error":"Token is not valid"}
    except Exception as e:
        return {"error":f"Something went wrong {str(e)}"}

# POST - Registers the user with required parameters : Login not required
@api_view(["POST"])
def signup(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            email = data.get('email', '')
            full_name = data.get('full_name', '')
            password = data.get('password', '')
            role = data.get('role', '')
            # Check for validation
            if (email == None or email == '') or (full_name == None or full_name == '') or (password == None or password == '') or (role == None or role == ''):
                data = {"error":"none fields","message":"Please enter details"}
                return JsonResponse(data)
            data = {"success": "success"}
            # Check the User's email already exists
            try:
                CustomUser.objects.get(email=email)
                return JsonResponse({'error': 'user already exists', 'message': 'User with this email already exists'}, status=400)
            except Exception as e:
                pass
                # Creating a new user
                user = CustomUser(email=email)
                user.full_name = full_name
                user.role = role
                user.set_password(password)
                user.save()

                if role == 'librarian':    
                    user.verified = False
                    user.save()           
                    data = {"success": "Registration successful"}
                    return JsonResponse(data)
                
                user = authenticate(email=email, password=password)
                # Checking password
                if user:
                    # Logging in user with password
                    refresh = RefreshToken.for_user(user)
                    data = {"success": "user created successfully","access": str(refresh.access_token),"refresh": str(refresh)}
                    return JsonResponse(data)
                else:
                    # Authentication failed password is invalid
                    data = {"error": "authentication failed","message": "Authentication failed"}
                    return JsonResponse(data)
        else:
            data = {"error":"method not allowed","message": "Method not allowed"}
            return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": f"Something went wrong : {str(e)}"})

# POST - Logging in user with required parameters : Login not required
@api_view(["POST"])
def login(request):
    if request.method == "POST":
        # Getting user data
        data = json.loads(request.body)
        email = data.get('email','')
        password = data.get('password','')
        try:
            if (email == None or email == '') or (password == None or password == ''):
                data = {"error":"none fields","message":"Email and password are required"}
                return JsonResponse(data)
            # Searching user with phone number
            user = authenticate(email=email, password=password)
            # Checking password
            if user:
                if user.role == "librarian" and not user.verified:
                    return JsonResponse({"error":"Please verify before continuing"})
                try:
                    ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
                    if ip_address:
                        ip_address = ip_address.split(',')[0]
                    else:
                        ip_address = request.META.get('REMOTE_ADDR')
                    response = requests.get(f"http://ip-api.com/json/{ip_address}")
                    data = response.json()
                    if(data["status"] == "success"):
                        city = data["city"]
                        state = data["regionName"]
                        pincode = data["zip"]
                        new_address = Address(user=user,city=city, state=state, pincode=pincode)
                        new_address.save()
                except Exception as e:
                    return JsonResponse({"error": str(e)})
                # Logging in user with password
                refresh = RefreshToken.for_user(user)
                data = {"success":"success","access": str(refresh.access_token),"refresh": str(refresh)}
                return JsonResponse(data)
            else:
                # Authentication failed password is invalid
                data = {"error": "authentication failed","message": "Please enter valid email and password"}
                return JsonResponse(data)
        except:
            # User not found
            user = None
        if user is None:
            data = {"error": "User not found","message":"User not found"}
            return JsonResponse(data)
    else:
        data = {"error": "Method not Allowed","message":"Method not Allowed"}
        return JsonResponse(data)

@api_view(["GET"])
def get_user(request):
    try:
        token = request.GET.get('token')
        if not token:
            return JsonResponse({"error": "token not found"})
        result = verify_token(token)
        if "error" in result and result["error"]:
            return JsonResponse({"error": result["error"]})

        if "success" in result and result["success"] == True:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
            user_id = decoded_token["user_id"]
            try:
                user = CustomUser.objects.get(id=user_id)
            except:
                user = None
            if user is not None:
                data = {"email": user.email, "name": user.full_name}
                return JsonResponse(data)
            else:
                return JsonResponse({"error": "User not found"})
        else:
            return JsonResponse({"error": "Authentication failed"})
    except Exception as e:
        return JsonResponse({"error": f"Something went wrong {str(e)}"})
    

@api_view(["GET"])
def getAllUser(request):
    try:
        token = request.GET.get('token')
        if not token:
            return JsonResponse({"error": "token not found"})
        result = verify_token(token)
        if "error" in result and result["error"]:
            return JsonResponse({"error": result["error"]})

        if "success" in result and result["success"] == True:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
            try:
                user = CustomUser.objects.all()
            except:
                user = None
            if user is not None:
                data = {"email": user.email, "name": user.full_name}
                return JsonResponse(data)
            else:
                return JsonResponse({"error": "User not found"})
        else:
            return JsonResponse({"error": "Authentication failed"})
    except Exception as e:
        return JsonResponse({"error": f"Something went wrong {str(e)}"})



@api_view(["GET"])
def profile(request):
    get_profile = Address.objects.get()
    context  = {
        'get_profile': get_profile
    }
    return JsonResponse(context)
    

# POST - adds a new address : Login Required
@api_view(["POST"])
def addAddress(request):
    if request.method == "POST":
        # Fetching the addresses
        token = request.query_params.get('token')
        if token:
            try:
                decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
                user_id = decoded_token["user_id"]
                user = CustomUser.objects.get(id=user_id)
            except Exception as e:
                data = {"error": "Authentication error"}
                return JsonResponse(data)
        address_count = Address.objects.filter(user=user_id).count()
        # max limit of addresses is 5
        if address_count >= 5:
            data = {"error": "You can add upto 5 addresses"}
            return JsonResponse(data)
        data = json.loads(request.body)
        address = data.get("address")
        city = data.get("city")
        state = data.get("state")
        pincode = data.get("pincode")
        # Creating a new address object
        if address == None or city == None or state == None or pincode == None:
            data = {"Error":"Please enter details"}
            return JsonResponse(data)
        new_address = Address(user=user, address=address, city=city, state=state, pincode=pincode)
        # Saving the new address
        new_address.save()
        data = {"success": "Addresses added successfully"}
        return JsonResponse(data)
    else:
        # Method Not Allowed
        data = {"error": "Method Not Allowed"}
        return JsonResponse(data)

# POST - Updates as Address with a required parameter address_id : Login Required
@api_view(["POST"])
def updateAddress(request):
    if request.method == "POST":
        try:
            # Get address object using address_id
            data = json.loads(request.body)
            address_id = data.get("address_id")
            address = Address.objects.get(id=address_id)
            # Updating address
            if data.get("address") is not None and data.get("address") != "null":
                address.address = data.get("address")
            if data.get("city") is not None and data.get("city") != "null":
                address.city = data.get("city")
            if data.get("pincode") is not None and data.get("pincode") != "null":
                address.pincode = data.get("pincode")
            if data.get("state") is not None and data.get("state") != "null":
                address.state = data.get("state")
            address.save()
            data = {"success": "address updated successfully"}
            return JsonResponse(data)
        except Address.DoesNotExist:
            # Address Not Found
            data = {"error": "Address does not exist"}
            return JsonResponse(data)
    else:
        # Method Not Allowed
        data = {"error": "Method Not Allowed"}
        return JsonResponse(data)
    
# DELETE - Delete Address by id
@api_view(["DELETE"])
def deleteAddress(request, id):
    token = request.query_params.get("token")
    if token:
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
            user_id = decoded_token["user_id"]
            try:
                address = Address.objects.get(id=id)
                if user_id == address.user.id:
                    address.delete()
                    data = {"success":f"Address Delete Successfully"}
                    return JsonResponse(data)
                else:
                    data = {"error":"Authentication Error"}
                    return JsonResponse(data)
            except Address.DoesNotExist:
                data = {"error":"Address does not exist"}
                return JsonResponse(data)
        except Exception as e:
            data = {"error":"Authentication Error"}
            return JsonResponse(data)
    else:
        data = {"error": "Authentication Error"}
        return JsonResponse(data)

# GET - Returns all addresses - Login Required
@api_view(["GET"])
def getAllAddresses(request):
        token = request.GET.get('token')
        data = None
        if token:
            try:
                decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
                token_user_id = decoded_token["user_id"]
                all_addresses = Address.objects.filter(user=token_user_id)
                try:
                    user = CustomUser.objects.get(id=token_user_id)
                except:
                    user = None

                if all_addresses.count() > 0:
                    serialized_obj = serializers.serialize('json',queryset=all_addresses)
                    data = {"success":serialized_obj}
                    if user:
                        data["name"] = user.username
                        data["email"] = user.email
                        data["phone_number"] = user.phone_number
                else:
                    data = {"empty": "No addresses were found"}
                return JsonResponse(data)
            except Exception as e:
                data = {"error": "Authentication error"}
                return JsonResponse(data)
        else:
            data = {"error":"Authentication Failed"}
            return JsonResponse(data)


@api_view(["GET"])        
def profile(request):
    token = request.GET.get('token')
    if not token:
            return JsonResponse({"error": "Invalid token"})
    result = verify_token(token)
    if "error" in result and result["error"]:
        return JsonResponse({"error": result["error"]})
    
    if "success" in result and result["success"] == True:
        decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
        user_id = decoded_token["user_id"]
        data = None
        try:
            user = CustomUser.objects.get(id=user_id)
        except:
            user = None
        if user is None:
            data = {"error":"User not found"}
            return JsonResponse(data, safe=False)
        data = {
            "phone_number": str(user.phone_number),
            "email": str(user.email),
            "username": str(user.username),
        }
        return JsonResponse(data, safe=False)
    return JsonResponse({"error":"Authentication failed"}, safe=False)

@api_view(["POST"])        
def updateProfile(request):
    token = request.query_params.get('token')
    data = json.loads(request.body)
    if token:
        decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
        url = BASE_URL + "api/token/verify/"
        headers = {"Authorization":f"bearer {token}"}
        body = {"token":token}
        result = requests.post(url, headers=headers,data=body)
        if result.status_code == 200:
            user_id = decoded_token["user_id"]
            try:
                user = CustomUser.objects.get(id=user_id)
            except:
                user = None
            if user is None:
                data = {"error":"User not found"}
                return JsonResponse(data, safe=False)
            if data.get("email") != None or data.get("email") != "null": user.email= data.get("email")
            if data.get("username") != None or data.get("username") != "null": user.username = data.get("username")
            user.save()
            data = {"success":"Profile updated successfully"}
        return JsonResponse(data, safe=False)
    return JsonResponse("DATA", safe=False)

# GET - Check if user is Authenticated - returns success:True if user is authenticated
@api_view(["GET"])
def checkUserIsSuperUser(request):
    try:
        token = request.GET.get("token")
        if not token:
            return JsonResponse({"error": "Invalid token"})
        result = verify_token(token)
        if "error" in result and result["error"]:
            return JsonResponse({"error": result["error"]})

        if "success" in result and result["success"] == True:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            user_id = decoded_token["user_id"]
            try:
                user = CustomUser.objects.get(id=user_id)
                if user.is_superuser:
                    return JsonResponse({"success": True})
                else:
                    return JsonResponse({"error":"Authentication failed"})
            except:
                user = None
                return JsonResponse({"error":"Authentication failed"})
        else:
            return JsonResponse({"error":"Authentication failed"})
    except Exception as e:
        print("error: " + str(e))
        return JsonResponse({"error":str(e)})

