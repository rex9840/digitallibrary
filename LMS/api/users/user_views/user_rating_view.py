from rest_framework import viewsets
from rest_framework.decorators import action

from api.users.user_serializers.user_rating import UserRatingPost
from ..user_serializers.user_rating import UserRating , Users
from ...models import Resources
from ..models import UserResourceInteraction
from rest_framework.permissions import IsAuthenticated 
from django.http import JsonResponse


class UserRatingViewSet(viewsets.ModelViewSet):
    queryset = UserResourceInteraction.objects.all()
    http_method_names = ['get','post']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserRatingPost
        return UserRating 


    def create(self, request, *args, **kwargs): 
        if not request.user.is_authenticated:
            return JsonResponse({'message': 'please login'}, status=403)
        
        user_id = Users.objects.get(id=request.user.id)
        resource_id = Resources.objects.get(resource_id=request.data['resource_id'])
        rating = request.data['rating']
        
        serilizer = UserRatingPost(data={'user_id':user_id.id, 'resource_id':resource_id.resource_id, 'rating':rating})
        if serilizer.is_valid(): 
            serilizer.save()
            return JsonResponse(serilizer.data, status=201) 
        return JsonResponse(serilizer.errors, status=400) 


        
 
    @action(detail=True, methods=['GET'])
    def user_rating(self, request,pk=None):
        user_rating = UserResourceInteraction.objects.filter(user_id=pk) 
        serializer = UserRating(user_rating, many=True)
        return JsonResponse(serializer.data, safe=False)
