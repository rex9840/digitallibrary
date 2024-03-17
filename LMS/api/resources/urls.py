from django.urls import path,include
from .views import * 
from rest_framework import routers 



router = routers.DefaultRouter()
router.register('details',ResourcesViewSet, basename='resource_details')
router.register('create',ReourcesCreateViewSet, basename='create_resource')
router.register('tags',TagsViewSet , basename="tags")

urlpatterns = [ 
    path('resources/',include(router.urls)),
]
