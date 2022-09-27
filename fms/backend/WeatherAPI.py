import requests
def getRainfallData():
    weather_request = "https://api.weatherapi.com/v1/current.json?key=2bc1a16f6bd948e7add30738202704&q=18.442928,73.763685"
    weather_data = requests.get(weather_request).json()
    lastHourRainfall = weather_data['current']['precip_mm']
    return lastHourRainfall