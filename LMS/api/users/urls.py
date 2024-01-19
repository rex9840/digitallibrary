
from django.urls import path, include
from . import views
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'register',views.RegisterView, basename='register')



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    path(r'users/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


