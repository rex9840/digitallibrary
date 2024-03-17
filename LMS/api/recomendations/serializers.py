from rest_framework import serializers
from ..resources.serializers import ResourcesSerializer 
from ..models import Resources,Users , UserResourceInteraction


class RecomendationsSerializer(serializers.Serializer): 
    user_id = serializers.IntegerField()
    resources = ResourcesSerializer(many=True)
    class Meta:
        fields = ['user_id','resources'] 





