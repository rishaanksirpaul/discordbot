import requests


def weatherBot(city_name):

    api_key = "69730d7673793ac769f9600a8447adad"

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    result = requests.get(url)

  
    weather = result.json()['weather'][0]['main']

    max_temp = result.json()['main']['temp_max']

    min_temp = result.json()['main']['temp_min']

    pressure = result.json()['main']['pressure']

    humidity = result.json()['main']['humidity']

    wind_speed = result.json()['wind']['speed']

    visibility = result.json()['visibility']

    return f"The main weather is {weather}, the maximum temperature is {max_temp}K and the minimum temperature is {min_temp}K, the pressure is {pressure}db and the humidity is {humidity}, the wind speed is {wind_speed}m/s while the visibility is {visibility}deg"