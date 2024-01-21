from .users import urls as user_urls
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ 
    path('', include(user_urls)),
]
