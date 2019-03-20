import requests
from flask import current_app

def weather_by_city(city_name):
    wearther_url = current_app.config["WEATHER_URL"]
    params = {
        'key': current_app.config["WEATHER_API_KEY"],
        'q': city_name,
        'format' : 'json',
        'num_of_days': 1,
        'lang' : 'ru'
    }
    try:
        result = requests.get(wearther_url, params=params)
        
        #result.raise_for_status()
        
        wearther = result.json()
        if 'data' in wearther:
            if 'current_condition' in wearther['data']:
                try:
                    return wearther['data']['current_condition'][0]
                except (IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        print('Network error')
    return False

if __name__ == "__main__":
    w = weather_by_city("Moscow, Russia")
    print(w)
