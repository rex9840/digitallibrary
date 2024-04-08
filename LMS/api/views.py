from django.shortcuts import render
from .recomendations.recomendation import get_recommendations, recomendation_cluster_tabel

def test(request): 
    recommendations = get_recommendations(25)
    recomendation_table = recomendation_cluster_tabel()
    data = {
            'recomendation_table': recomendation_table.to_html(), 

            'recomendations': recommendations.to_html()
            }
    return render(request, 'test.html', data)
