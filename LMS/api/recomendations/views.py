from django.shortcuts import render
from rest_framework import viewsets
from .recomendation import get_recommendations , recomendation_cluster_tabel 
from api.models import Users , UserResourceInteraction , Resources 
from .serializers import Recomendations





