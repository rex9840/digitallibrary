
from contextlib import redirect_stdout
from http.client import METHOD_NOT_ALLOWED, responses
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
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get','delete', 'patch']

    def get_queryset(self):
        if self.request.user.is_authenticated and not self.request.user.is_admin:
            user_id = self.request.user.id
            return Users.objects.filter(id=user_id)

        if self.request.user.is_admin and self.request.method == 'GET':
            return Users.objects.all() 

        else :
            return Users.objects.none()


    def destroy(self, request, *args, **kwargs):
        if request.user.is_admin:
            return JsonResponse({'message': 'please use admin pannel'}, status=403)

        user = Users.objects.get(id=request.user.id)
        user.delete()
        return JsonResponse({'message': 'User was deleted successfully!'}, status=204) 
   

    def partial_update(self, request,pk=None):

        if request.user.is_admin:
            return JsonResponse({'message': 'please use admin pannel'}, status=403) 
       
        user = Users.objects.get(id=pk)

        if user.id != request.user.id:
            return JsonResponse({'message': 'you are not allowed to update this user'}, status=403) 

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400) 




