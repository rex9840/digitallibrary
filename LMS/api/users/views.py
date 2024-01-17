from typing import Generic
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view
from rest_framework.views import csrf_exempt


from .__models__.user import User
from .__serializers__.user import UserSerializer

from rest_framework import viewsets


# class based view

#class UserlistView(APIView): 
#    def post(self,request): 
#        data_request = JSONParser().parse(request)
#        user_serializer = UserSerializer(data=data_request)
#        if user_serializer.is_valid():
#            user_serializer.save()
#            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
#        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#

class UserAddView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    @action(detail=True, methods=['post'])
    def add(self,request):
        data_request = JSONParser().parse(request)
        user_serializer = UserSerializer(data=data_request)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class GetUser(APIView): 
    def get(self,request,UserId): 
        user = User.objects.filter(UserID=UserId).first()
        if user:
            user_serializer = UserSerializer(user)
            user_data = user_serializer.data
            del user_data['Password']
            return JsonResponse(user_data, status=status.HTTP_200_OK)
        return JsonResponse({"ERROR":'USER DOESNT EXIT'}, status=status.HTTP_400_BAD_REQUEST)




@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer  = UserSerializer(users, many=True)
        for x in serializer.data:
            del x['Password']
        return JsonResponse(serializer.data, safe=False)
# Create your views here.