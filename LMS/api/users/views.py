from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.views import csrf_exempt
from django.shortcuts import get_object_or_404,render
from .__serializers__.user_serializer import UserSerializer, RegisterSerializer

from rest_framework import viewsets
from rest_framework.response import Response 

from .models import Users 

from django.core.files.storage import default_storage


class RegisterView(viewsets.ModelViewSet): 
    queryset = Users.objects.all()
    serializer_class = RegisterSerializer
    @action(detail=True, methods=['post'])
    def register(self,request):
        data_request = JSONParser().parse(request)
        user_serializer = RegisterSerializer(data=data_request)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)






