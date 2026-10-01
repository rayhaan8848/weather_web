from django.shortcuts import render
import requests
from decouple import config

# Create your views here.
def index(request):
    API_KEY=config('API_KEY')
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='Kathmandu'
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    data = requests.get(url, {'units': 'metric'}).json()

    # Main weather information
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']

    humidity = data['main']['humidity']
    pressure = data['main']['pressure']

    # Weather condition
    des = data['weather'][0]['description']
    icon = data['weather'][0]['icon']

    # Wind
    wind = data['wind']['speed']

    # Visibility
    # OpenWeather gives visibility in meters
    visibility = data['visibility'] / 1000

    # City
    city_name = data['name']


    context = {
        'temp': temp,
        'city': city_name,
        'humidity': humidity,
        'des': des,
        'icon': icon,

        'feels_like': feels_like,
        'temp_min': temp_min,
        'temp_max': temp_max,

        'pressure': pressure,
        'wind': wind,
        'visibility': visibility,
    }
    return render(request, "index.html",context)

