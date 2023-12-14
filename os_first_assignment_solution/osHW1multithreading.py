import json
from concurrent.futures import ThreadPoolExecutor
import threading

def process_city(city_data):
    city_name, city_info = city_data
    thread_id = threading.get_ident()
    print(f"Thread-{thread_id}")
    print(f"Processing {city_name} weather data:")
    for key, value in city_info.items():
        print(f"{key}: {value}")
    print()

with open("/home/rey1/Documents/weather_data.json","r") as file:
    data = json.load(file)
    
city_data_list = [(city_name, city_info) for city_name, city_info in data.items()]

with ThreadPoolExecutor(max_workers = 8, thread_name_prefix='MyThread') as executor:
    for city_data in city_data_list:
        executor.submit(process_city,city_data)
















