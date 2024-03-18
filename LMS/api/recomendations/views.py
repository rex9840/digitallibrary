from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .recomendation import get_recommendations , recomendation_cluster_tabel 
from api.models import Users, Resources,UserResourceInteraction
from django.http import JsonResponse
from rest_framework.decorators import action 
from rest_framework.permissions import IsAuthenticated
from ..resources.serializers import ResourcesSerializer



class RecomendationsViewSet(viewsets.ViewSet):
    serializer_class = ResourcesSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        
        try:

            user_id = Users.objects.get(id=request.user.id).id
            resource_id = get_recommendations(user_id)["resource_id"].to_list() 
            clustered_id = recomendation_cluster_tabel().iloc[0].to_list()
            
            resource_id = resource_id + clustered_id

            visited_id = UserResourceInteraction.objects.filter(user_id=user_id).values_list('resource_id', flat=True)
            
            visited_data = Resources.objects.filter(resource_id__in=visited_id)
            visited_data = ResourcesSerializer(visited_data, many=True).data
            
            visited_id = list(set(visited_id)) 

            recomendation_id = [x for x in resource_id if x not in visited_id]
            
            recomendation_resources = Resources.objects.filter(resource_id__in=recomendation_id)
            recomendation_resources = ResourcesSerializer(recomendation_resources, many=True).data
        

            data = {
                'user_id': user_id,
                'recomendation_resources': recomendation_resources,
                'visited_resources': visited_data,
            } 


            return JsonResponse(data, safe=False)

        except IndexError: 
            
            recomendation_id = recomendation_cluster_tabel().iloc[:2].values.tolist()
            recomendation_id = [item for sublist in recomendation_id for item in sublist]
            recomendation_resources = Resources.objects.filter(resource_id__in=recomendation_id)
            recomendation_resources = ResourcesSerializer(recomendation_resources, many=True).data
            data = {
                'user_id': user_id,
                'recomendation_resources': recomendation_resources,
            }
            return JsonResponse(data, safe=False) 


