from rest_framework import serializers
from datetime import datetime
from api.users.models import Users
import bcrypt
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model  = Users
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    address = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=10)
    school_id = serializers.IntegerField(required=True)
    is_teacher = serializers.BooleanField(default=False)

    class Meta:
        model = Users
        exclude = ['ID']
