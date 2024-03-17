from rest_framework import viewsets
from rest_framework.decorators import action

from api.users.user_serializers.user_rating import UserRatingPost
from ..user_serializers.user_rating import UserRating 
from ..models import UserResourceInteraction
from rest_framework.permissions import IsAuthenticated 
from django.http import JsonResponse


class UserRatingViewSet(viewsets.ModelViewSet):
    http_method_names = ['GET', 'POST']
    queryset = UserResourceInteraction.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserRatingPost
        return UserRating 


    def create(self, request, *args, **kwargs): 
        permission_classes = [IsAuthenticated]
        if not request.user.is_authenticated:
            return JsonResponse({'message': 'please login'}, status=403)
        return super().create(request, *args, **kwargs)
    
    
    @action(detail=True, methods=['GET'])
    def user_rating(self, request,pk=None):
        user_rating = UserResourceInteraction.objects.filter(user_id=pk) 
        serializer = UserRating(user_rating, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)
    
