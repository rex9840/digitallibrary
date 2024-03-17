from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .recomendation import get_recommendations , recomendation_cluster_tabel 
from api.models import Users , UserResourceInteraction , Resources 
from .serializers import RecomendationsSerializer




class RecomendationsViewSet(viewsets.ViewSet):
    serializer_class = RecomendationsSerializer
    http_method_names = ['GET']
    queryset = Users.objects.all()

