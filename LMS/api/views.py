from django.shortcuts import render
from .recomendations.recomendation import get_recommendations


def test(request): 
    recommendations = get_recommendations(2)
    data = {
            'recomendations': recommendations.to_html()
            }
    return render(request, 'test.html', data)
