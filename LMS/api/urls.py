from .users import urls as user_urls
from django.urls import include,path



urlpatterns = [ 
    path('', include(user_urls)),
]
