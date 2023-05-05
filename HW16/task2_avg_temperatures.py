import requests
import threading
import multiprocessing

API_URL = "https://api.open-meteo.com/v1/forecast"

cities = [
    {"name": "Kyiv", "lat": 50.45, "lon": 30.52},
    {"name": "Tokyo", "lat": 35.69, "lon": 139.69},
    {"name": "Seoul", "lat": 37.57, "lon": 126.98},
    {"name": "New-York", "lat": 40.71, "lon": -74.01},
    {"name": "London", "lat": 51.51, "lon": -0.13},
]

def get_weather(city):
    params = {"latitude": city["lat"], "longitude": city["lon"], "hourly": "temperature_2m"}
    response = requests.get(API_URL, params=params)
    if response.ok:
        data = response.json()
        temperatures = data["hourly"]["temperature_2m"]
        avg_temp = sum(temperatures) / len(temperatures)
        return avg_temp
    else:
        print(f"Failed to get weather data for {city['name']}")
        return None


# using threading
threads = []
for city in cities:
    t = threading.Thread(target=get_weather, args=(city,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# using multiprocessing
if __name__ == '__main__':
    processes = [multiprocessing.Process(target=get_weather, args=(city,)) for city in cities]
    for process in processes:
        process.start()
    for process in processes:
        process.join()


# # calculate average temperatures and find the hottest city
avg_temperatures = {}
for city in cities:
    avg_temperatures[city["name"]] = get_weather(city)

hottest_city = max(avg_temperatures, key=avg_temperatures.get)

# print results
print("Average temperatures:")
for city, temp in avg_temperatures.items():
    print(f"{city}: {temp}")
print(f"The hottest city is {hottest_city}")
