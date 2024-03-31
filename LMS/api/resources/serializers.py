from rest_framework import serializers
from .models import Resources, Tags
from ..users.models import Users
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
        tag_list = []
        for tag in instance.tags.all():
            tag_list.append(tag.tag_name)
        representation['tags'] = tag_list
        rating = UserResourceInteraction.objects.filter(resource_id=instance.resource_id).aggregate(Avg('rating'))
        representation['rating'] = rating['rating__avg']
        return representation


class ResourceCreateSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True,queryset=Tags.objects.all())
    class Meta: 
        model = Resources
        fields = ['name','description','tags','resource_image','resource_file']




