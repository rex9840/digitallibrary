from django.urls import path,include 
from rest_framework import routers
from .views import RecomendationsViewSet



router = routers.DefaultRouter()
router.register('recomendations',RecomendationsViewSet,'recomendations')


urlpatterns = [
    path('home/',include(router.urls)),
]


