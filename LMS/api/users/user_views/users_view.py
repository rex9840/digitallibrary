
from http.client import METHOD_NOT_ALLOWED
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import csrf_exempt
from api.users.user_serializers.user_serializer import *
from api.users.user_models.user_model import Users
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny


class UsersCreate(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = RegisterSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    


class UserView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    http_method_names = ['get','delete','patch']
    def list(self, request):
        data = Users.objects.all() 
        serializer = UserSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False,status=200)
