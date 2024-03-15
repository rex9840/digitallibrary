from django.urls import path,include
from .views import * 
from rest_framework import routers 



router = routers.DefaultRouter()
router.register('details',ResourcesViewSet, basename='details')
router.register('tags',TagsViewSet , basename="tags")
urlpatterns = [ 
    path('resources/',include(router.urls)),
]
