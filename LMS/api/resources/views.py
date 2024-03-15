from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.exceptions import JsonResponse
from .models import Resources,Tags
from api.models import UserResourceInteraction
from .serializers import ResourcesSerializer, TagSerializer
from rest_framework.permissions import IsAuthenticated


class TagsViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    http_method_names = ['get','post']
    permission_classes = [IsAuthenticated]
    queryset = Tags.objects.all()



class ResourcesViewSet(viewsets.ModelViewSet): 
    
    serializer_class = ResourcesSerializer
    http_method_names = ['get','post','patch','delete']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        
        if self.request.user.is_admin and self.request.method == 'GET':
            return Resources.objects.all() 
        
        if self.request.user.is_authenticated:
            user_id = request.user.id
            return Resources.objects.filter(uploaded_by=user_id)


    def list(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = ResourcesSerializer(queryset,many=True)
        return JsonResponse(serializer.data,status=200, safe=False)

    def create(self,request,*args,**kwargs):
        serializer = ResourcesSerializer(data=request.data)
        serializer.validated_data['uploaded_by'] = request.user.id
        serializer.data['rating'] = 0
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

        
    def destroy(self, request, *args, **kwargs):
        if request.user.is_admin:
            return JsonResponse({'message': 'please use admin pannel'}, status=403)

        resource = Resources.objects.get(resource_id=request.data['resource_id'])
        if resource.uploaded_by != request.user.id:
            return JsonResponse({'message': 'You are not authorized to delete this resource'}, status=403)
        resource.delete()
        return JsonResponse({'message': 'Resource was deleted successfully!'}, status=204) 
