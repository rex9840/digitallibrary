from django.shortcuts import render
from django.http.response import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView



from .models import *
from .serializers import * 


import re

# Create your views here.


# class based view

class UserlistView(APIView): 
    def post(self,request): 
        data_request = JSONParser().parse(request)
        user_serializer = UserSerializer(data = data_request)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer  = UserSerializer(users, many=True)
        for x in serializer.data:
            del x['Password']

        return JsonResponse(serializer.data, safe=False)






