from .users import urls as user_urls
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from .views import test
from  .recomendations import urls as recomendations_urls
from .resources import urls as resources_urls


urlpatterns = [ 
    path('', include(user_urls)),
    path('test/', test, name='test'),    
    path('', include(recomendations_urls)),
    path('', include(resources_urls)),
    path('',include(user_urls)),
]
