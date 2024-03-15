from rest_framework import serializers
from .models import Users , UserResourceInteraction , Resources




class ResourceSerializer(serializers.Serializer): 
    class Meta:
        model = Resources 
        fields = __all__



class Recomendations(serializers.Serializer): 
    user_id = serializers.IntegerField()
    resources = ResourceSerializer(many=True)
    class Meta:
        fields = ['user_id','resources'] 





