#!/usr/bin/env python3

#interview question

import requests
from pprint import pprint

def fetch_weather_data(keyword):
    data_url = "https://jsonmock.hackerrank.com/api/weather/search?name="
    page = 1
    data = []
    
    while True:
        response = requests.get(data_url + keyword + "&page=" + str(page))
        response_data = response.json()
        data.extend(response_data['data'])
        
        if page > response_data['total_pages']:
            break
        page += 1
    processed_data = []
    for response in response_data:
        name = response['name']
        temperature = response['weather'].replace(' degree', '')
        #name = response.get('name')
        #temperature = reponse.get('weather').replace(' degree', '')
        status = response['status']
        for x in status:
            if 'Wind' in status:
                wind = x.split(' :')[1].replace('Kmph', '')
            if 'Humidity' in status:
                humidity = x.split(' :')[1].replace('%', '')
            processed_data.append(f"{name},{temperature},{wind},{humidity}")
    return processed_data

if __name__ == "__main__":
    weather_data = fetch_weather_data("all")
    pprint(weather_data)
