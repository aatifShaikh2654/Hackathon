from rest_framework import serializers
from .models import CustomUser


# Here Define all your model serializers
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"