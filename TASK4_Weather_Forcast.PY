#CODSOFT TASK 4
import requests

api_key = 'f4993ffd325b79e14a4455d1d969161b'

def get_weather_data(city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
  
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print("Error: Unable to fetch weather data from open weather map \n You should try to replace the API_KEY if it's still not works for different location ")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def display_weather_data(data):
    if data:
    
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

      
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("No weather data to display.")

def main():
    print("Welcome to the Weather Forecast Application!")
    city_name = input("Please enter the name of a city or your location: ")
    weather_data = get_weather_data(city_name)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()
