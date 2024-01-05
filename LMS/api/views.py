from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status 
 
from .models import *
from .serializers import * 

# Create your views here.

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serialiser  = UserSerializer(users, many=True)
        return JsonResponse(serialiser.data, safe=False)
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data) 
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

