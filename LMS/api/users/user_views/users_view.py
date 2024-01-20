
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from api.users.user_serializers.user_serializer import *
from api.users.user_models.user_model import Users
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import action


class Users(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        elif self.request.method == 'POST':
            return RegisterSerializer
    
    @action(detail=True, methods=['GET'])
    def user_list(self, request):
        queryset = Users.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    @action(detail=True, methods=['POST'])
    def user_create(self, request, pk=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

