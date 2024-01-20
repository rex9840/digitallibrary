from rest_framework import serializers
from datetime import datetime
from django.contrib.auth.hashers import make_password
from api.users.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Users
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):

    is_teacher = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = Users
        exclude = ['ID']

    def create(self, validated_data):
        return super().create(validated_data)
