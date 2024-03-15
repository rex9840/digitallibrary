from rest_framework import serializers 
from ..models import UserResourceInteraction
from .user_serializer import UserSerializer
from ...resources.serializers import  ResourcesSerializer
from ...models import Resources, Users

class UserRating(serializers.Serializer):
    resource_id = serializers.PrimaryKeyRelatedField(queryset=Resources.objects.all())
    user_id = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    rating = serializers.FloatField()
    class Meta:
        model = UserResourceInteraction
        fields = ['resource_id','user_id','rating']
    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        resource = Resources.objects.get(resource_id=instance.resource_id.resource_id)
        user = Users.objects.get(id=instance.user_id.id)
        representation['resource_name'] = resource.name
        representation['user_name'] = user.first_name + ' ' + user.last_name
        tags = Resources.objects.get(resource_id=instance.resource_id.resource_id).tags.all()
        representation['tags'] = list(tags.values_list('tag_name', flat=True))
        return representation



class UserRatingPost(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    resource_id = serializers.PrimaryKeyRelatedField(queryset=Resources.objects.all())
    class Meta:
        model = UserResourceInteraction
        fields = ['resource_id','user_id','rating']
