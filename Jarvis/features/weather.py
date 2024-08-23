import requests
from Jarvis.config import config



def fetch_weather():
    """
    City to weather
    :param city: City
    :return: weather
    """
    

    complete_url = "https://api.open-meteo.com/v1/gfs?latitude=27.70&longitude=85.43&current_weather=true" #this api probably isnt functional anymore need to try new one
    
    response = requests.get(complete_url)       

    
    if (response.ok):
        city_weather_data = response.json()
        '''main_data = city_weather_data["main"]
        weather_description_data = city_weather_data["weather"][0]
        weather_description = weather_description_data["description"]
        current_temperature = main_data["temp"]
        current_pressure = main_data["pressure"]
        current_humidity = main_data["humidity"]
        wind_data = city_weather_data["wind"]
        wind_speed = wind_data["speed"]'''
        current_temperature= city_weather_data['current_weather']['temperature'] #only temp no weather
        '''
        final_response = f"""
        The weather in {city} is currently {weather_description} 
        with a temperature of {current_temperature} degree celcius, 
        atmospheric pressure of {current_pressure} hectoPascals, 
        humidity of {current_humidity} percent 
        and wind speed reaching {wind_speed} kilometers per hour"""
        '''
        final_response=f"The current temperature is {current_temperature}"

        return final_response

    else:
        return "Sorry Sir, I couldn't find the city in my database. Please try again"