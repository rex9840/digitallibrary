from django.shortcuts import render
from .recomendations.data_preprocessing import data_preprocessing


def test(request): 
    recommendations = data_preprocessing()
    data = {
            'recomendations': recommendations.to_html()
            }
    return render(request, 'test.html', data)
