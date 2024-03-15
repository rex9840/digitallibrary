
from django.urls import path, include
from LMS.settings import BASE_DIR
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('details', views.UserView,'details')
router.register('create', views.UsersCreate,'create')
router.register('rating', views.UserRatingViewSet,'rating')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    path('users/', include(router.urls)),

]


