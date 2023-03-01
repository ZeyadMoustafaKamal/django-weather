from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests
from django.contrib import messages
# Create your views here.
def index(request):
    cities = City.objects.all()
    weathers = []
    if request.method == 'POST':
        form = CityForm(request.POST)
        city_name = request.POST['name']
        test_request = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0301e8ca4dbb4b384b45dc7b83cd867c'.format(city_name)).json()
        try:
            error = test_request['message']
            messages.error(request, "The city wasn't found")
        except NameError:
            form.save()
    else:
        form = CityForm
    for city in cities:
        r = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0301e8ca4dbb4b384b45dc7b83cd867c'.format(city)).json()
        
        weather ={
            'city':r['name'],
            'temp':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']
        }
        weathers.append(weather)
    context = {
        'weathers':weathers,
        'form':form
        }
    return render(request, 'index.html', context)