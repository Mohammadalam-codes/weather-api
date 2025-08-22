import requests

API_KEY = " df182cde018c4283b63131219252005"  # Replace with your actual WeatherAPI key
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather(city):
    params = {
        'q': city,
        'key': API_KEY
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city_name = data['location']['name']
        temp = data['current']['temp_c']
        description = data['current']['condition']['text']
        humidity = data['current']['humidity']
        wind_speed = data['current']['wind_kph']

        print(f"\nWeather in {city_name}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} kph")
    else:
        print("❌ Could not retrieve weather data.")

if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)
