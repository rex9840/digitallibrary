from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.exceptions import JsonResponse
from .models import Resources,Tags
from .serializers import ResourcesSerializer, TagSerializer, ResourceCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

class TagsViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    http_method_names  = ['get','post']
    permission_classes = [IsAuthenticated]
    queryset = Tags.objects.all()




class ReourcesCreateViewSet(viewsets.ModelViewSet):
    serializer_class = ResourceCreateSerializer
    http_method_names  = ['post']
    permission_classes = [IsAuthenticated]
    queryset = Resources.objects.all()

    def create(self,request,*args,**kwargs):
        serializer = ResourceCreateSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save(uploaded_by=request.user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



class ResourcesViewSet(viewsets.ModelViewSet): 
    http_method_names  = ['get','patch','delete']
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self,*args,**kwargs):
        if self.request.user.is_admin and self.request.method == 'GET':
            return Resources.objects.all()  
        return Resources.objects.filter(uploaded_by=self.request.user)


    def get_serializer_class(self): 
        if self.request.method == 'Patch':
            return ResourceCreateSerializer
        return ResourcesSerializer 



    def destroy(self, request,pk=None):
        resource = Resources.objects.get(resource_id=pk)

        if resource.uploaded_by.id != request.user.id:
            return JsonResponse({'message': 'You are not authorized to delete this resource'}, status=403)
        resource.delete()
        return JsonResponse({'message': 'Resource was deleted successfully!'}, status=204) 
    

    def partial_update(self, request,pk=None):
        resource = Resources.objects.get(resource_id=pk) 

        if resource.uploaded_by.id != request.user.id:
            return JsonResponse({'message': 'You are not authorized to update this resource'}, status=403)
        
        serializer = ResourceCreateSerializer(resource, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    

    @action(detail=False, methods=['GET'],permission_classes=[IsAuthenticated])
    def all_resources(self, request):
        resources = Resources.objects.all()
        serializer = ResourcesSerializer(resources, many=True)
        return JsonResponse(serializer.data, safe=False) 

