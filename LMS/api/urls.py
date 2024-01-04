from django.urls import path, include
from . import views



urlpatterns = [
    path('users/', views.user_list),
        

]


