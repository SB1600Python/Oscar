from django.shortcuts import render, redirect
import requests 
from weather.models import *
from weather.forms import *

# Create your views here.
def index(request):

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    appid = '22520a38955cb98f77c2fbbf6ee52a21'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid    
    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
            'id': city.id,
        }
        all_cities.append(city_info)

    return render(request, 'weather/index.html', {'title': 'Главная страница', 'all_info': all_cities, 'form': form})