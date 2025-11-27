import requests
import json

def get_weather_details(city_name, api_key):
    """
    Display weather details of a city using OpenWeatherMap API.
    
    Args:
        city_name (str): Name of the city to get weather for
        api_key (str): OpenWeatherMap API key
    
    Returns:
        dict: Weather data as JSON, or None if error occurs
    """
    # OpenWeatherMap API endpoint
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use metric units (Celsius)
    }
    
    try:
        # Send GET request to the API
        response = requests.get(base_url, params=params, timeout=10)
        
        # Check if the request was successful (status code 200)
        response.raise_for_status()
        
        # Parse JSON response
        weather_data = response.json()
        
        # Return the weather data
        return weather_data
        
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please check your network connection.")
        return None
        
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your network connection.")
        return None
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            print("Error: Invalid API key. Please check your API key.")
        elif e.response.status_code == 404:
            print(f"Error: City '{city_name}' not found. Please check the city name.")
        else:
            print(f"Error: HTTP {e.response.status_code} - {e}")
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred while making the request: {e}")
        return None
        
    except json.JSONDecodeError:
        print("Error: Invalid JSON response from API.")
        return None
        
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return None


def display_weather_json(weather_data):
    """
    Display weather data in a readable JSON format.
    
    Args:
        weather_data (dict): Weather data dictionary
    """
    if weather_data:
        # Format JSON with indentation for readability
        formatted_json = json.dumps(weather_data, indent=2, ensure_ascii=False)
        print("\n" + "="*60)
        print("Weather Details (JSON Format):")
        print("="*60)
        print(formatted_json)
        print("="*60 + "\n")
    else:
        print("No weather data to display.")


def main():
    """
    Main function to run the weather API program.
    """
    print("Weather API - City Weather Details")
    print("-" * 40)
    
    # API key - Replace with your actual OpenWeatherMap API key
    api_key = "5b54945900fa4db64d400472c9daaea1"
    
    # Get city name from user
    city_name = input("Enter the city name: ").strip()
    
    if not city_name:
        print("Error: City name cannot be empty.")
        return
    
    # Fetch weather details
    print(f"\nFetching weather data for {city_name}...")
    weather_data = get_weather_details(city_name, api_key)
    
    # Display the weather data in JSON format
    display_weather_json(weather_data)
    
    # Optional: Display a user-friendly summary
    if weather_data:
        try:
            print("Summary:")
            print(f"  City: {weather_data['name']}, {weather_data['sys']['country']}")
            print(f"  Temperature: {weather_data['main']['temp']}°C")
            print(f"  Description: {weather_data['weather'][0]['description'].title()}")
            print(f"  Humidity: {weather_data['main']['humidity']}%")
            print(f"  Wind Speed: {weather_data['wind']['speed']} m/s")
        except KeyError:
            print("Note: Could not display summary (missing data fields)")


if __name__ == "__main__":
    main()
