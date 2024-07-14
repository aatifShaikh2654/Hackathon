from django.http import JsonResponse
import requests

BASE_URL = "http://127.0.0.1:8000/"

def verify_token(token):
    try:
        if not token:
            return JsonResponse({"error":"Token is required"})
        url = BASE_URL + "api/token/verify/"
        headers = {"Authorization": f"Bearer {token}"}
        body = {"token":token}
        result = requests.post(url, headers=headers, data=body)
        if result.status_code == 200:
            return {"success":True}
        else:
            return {"error":"Token is not valid"}
    except Exception as e:
        return {"error":f"Something went wrong {str(e)}"}
        
