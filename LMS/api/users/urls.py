from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users/add',views.UserAddView)

urlpatterns = [
    path(r'^users/', views.user_list),
    path(r'^', include(router.urls)),
    #    path('users/add/',views.UserlistView.as_view()),
    path('users/<int:UserId>/',views.GetUser.as_view()),
]


