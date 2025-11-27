import requests
import json

def get_weather_details(city_name, api_key):
    """
    Display weather details of a city using OpenWeatherMap API.
    (Task 1: With basic error handling)
    """

    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    return weather_data


def display_weather_json(weather_data):
    formatted_json = json.dumps(weather_data, indent=2, ensure_ascii=False)
    print("\n" + "="*60)
    print("Weather Details (JSON Format):")
    print("="*60)
    print(formatted_json)
    print("="*60 + "\n")


def main():
    print("Weather API - City Weather Details")
    print("-" * 60)

    # 🔹 Replace with Your Active API Key
    api_key = "5b54945900fa4db64d400472c9daaea1"

    city_name = input("Enter the city name: ").strip()
    print(f"\nFetching weather data for {city_name}...")

    weather_data = get_weather_details(city_name, api_key)

    # 🔹 Basic error check
    if weather_data.get("cod") != 200:
        print("\n❌ Error:", weather_data.get("message", "Unknown error occurred"))
    else:
        display_weather_json(weather_data)


if __name__ == "__main__":
    main()
