import requests

def get_weather(city_name):
    geocoding_params = {
        'name': city_name,
        'count': 10,
        'language': 'en',
        'format': 'json'
    }
    geocoding_url = 'https://geocoding-api.open-meteo.com/v1/search'
    geocoding_response = requests.get(geocoding_url, params=geocoding_params)
    geocoding_data = geocoding_response.json()

    if 'results' not in geocoding_data:
        print(f'City {city_name} not found.')
        return

    location = geocoding_data['results'][0]
    latitude = location['latitude']
    longitude = location['longitude']

    weather_params = {
        'latitude': latitude,
        'longitude': longitude,
        'hourly': 'temperature_2m'
    }
    weather_url = 'https://api.open-meteo.com/v1/forecast'
    weather_response = requests.get(weather_url, params=weather_params)
    weather_data = weather_response.json()

    current_temperature = weather_data['hourly']['temperature_2m'][0]

    print(f'Temperature in {location["name"]}: {current_temperature}°C')

city_name = input('Enter the city name: ')
get_weather(city_name)
