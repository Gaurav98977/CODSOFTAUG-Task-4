#cod-soft task 4 
import requests
 

def get_weather_data(api_key, location):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": '4a5292bb6dcf7c56b44d1c3c25549ff9',
        #for other parameters values imperial for Fahrenheit
        "units": "metric"  
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data.get("cod") == 200:
            return data
        else:
            return None
    
    except requests.exceptions.RequestException as e:
        print("Error to fetch the API request:", e)
        return None


def display_weather(weather_data):
    if not weather_data:
        print("Weather data not available for the specified location.")
        return
    
    city_name = weather_data["name"]
    temperature = weather_data["main"]["temperature"]
    wind_speed = weather_data["wind"]["Speed"]
    description = weather_data["weather"][0]["Description"]
    humidity = weather_data["main"]["Humidity"]
    
    
    print(f"Weather in {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Description: {description.capitalize()}")
    print(f"Humidity: {humidity}%")

def main():
    api_key = "4a5292bb6dcf7c56b44d1c3c25549ff9" 
    
    while True:
        location = input("Enter a city name or zip code (for return type exit): ")
        
        if location.lower() == "exit":
            break
        
        weather_data = get_weather_data(api_key, location)
        display_weather(weather_data)

if __name__ == "__main__":
    main()