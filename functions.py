import requests
import geocoder
from math import radians, cos, sin, asin, sqrt

def whatCityWeather(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=4ebb48b17238d755e6e5120b459fde06&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        x = response.json()['main']['temp']
    return x


def getLoc(city):
    g = geocoder.osm(city)
    eee = g.latlng
    return eee


def haversine(lat1, lon1, lat2, lon2):

    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r


#print(whatCityWeather("Las Claritas"))

