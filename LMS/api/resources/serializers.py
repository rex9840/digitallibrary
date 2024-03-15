from rest_framework import serializers
from .models import Resources, Tags 
from api.models import UserResourceInteraction
from django.db.models import Avg

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['tag_id','tag_name']


class ResourcesSerializer(serializers.ModelSerializer):  
    tags = TagSerializer(many=True)
    resource_image = serializers.ImageField(max_length=None,use_url=True)
    resource_file = serializers.FileField(max_length=None,use_url=True)

    class Meta:
        model = Resources
        fields = ['resource_id','name','description','tags','resource_image','resource_file','uploaded_by']


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        rating = UserResourceInteraction.objects.filter(resource_id=instance.resource_id).aggregate(Avg('rating'))
        representation['rating'] = rating['rating__avg']
        return representation



