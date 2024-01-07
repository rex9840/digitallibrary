from django.urls import path, include
from . import views



urlpatterns = [
    path('users/', views.user_list),
    path('users/add/',views.UserlistView.as_view()),
    path('users/<int:UserId>/',views.GetUser.as_view()),
]


