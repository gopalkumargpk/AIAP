import requests
import json

def get_weather_details(city_name, api_key):
    """
    Retrieve weather details of a city using OpenWeatherMap API.
    (Task 3: Extract and Display Specific Data)
    
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
        # Send GET request to the API with timeout
        response = requests.get(base_url, params=params, timeout=10)
        
        # Check if the request was successful (status code 200)
        response.raise_for_status()
        
        # Parse JSON response
        weather_data = response.json()
        
        # Check if API returned an error in the JSON response
        if weather_data.get("cod") and str(weather_data.get("cod")) != "200":
            # API returned error code (e.g., 401 for invalid API key, 404 for city not found)
            if weather_data.get("cod") == 401:
                print("Error: Could not connect to API. Check your API key or network connection.")
            else:
                print("Error: Could not connect to API. Check your API key or network connection.")
            return None
        
        # Return the weather data
        return weather_data
        
    except requests.exceptions.Timeout:
        print("Error: Could not connect to API. Check your API key or network connection.")
        return None
        
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your API key or network connection.")
        return None
        
    except requests.exceptions.HTTPError as e:
        # Handle specific HTTP errors
        if e.response.status_code == 401:
            print("Error: Could not connect to API. Check your API key or network connection.")
        elif e.response.status_code == 404:
            # Check if it's an invalid API key or city not found
            try:
                error_data = e.response.json()
                if error_data.get("cod") == 401:
                    print("Error: Could not connect to API. Check your API key or network connection.")
                else:
                    print(f"Error: City '{city_name}' not found. Please check the city name.")
            except:
                print("Error: Could not connect to API. Check your API key or network connection.")
        else:
            print("Error: Could not connect to API. Check your API key or network connection.")
        return None
        
    except requests.exceptions.InvalidURL:
        print("Error: Could not connect to API. Check your API key or network connection.")
        return None
        
    except requests.exceptions.RequestException as e:
        print("Error: Could not connect to API. Check your API key or network connection.")
        return None
        
    except json.JSONDecodeError:
        print("Error: Could not connect to API. Check your API key or network connection.")
        return None
        
    except Exception as e:
        print("Error: Could not connect to API. Check your API key or network connection.")
        return None


def extract_and_display_weather(weather_data):
    """
    Extract specific fields from weather data and display them in a user-friendly format.
    
    Args:
        weather_data (dict): Weather data dictionary from API
    """
    if not weather_data:
        print("No weather data available to display.")
        return
    
    try:
        # Extract specific fields from the API response
        city = weather_data.get("name", "N/A")
        temperature = weather_data.get("main", {}).get("temp", "N/A")
        humidity = weather_data.get("main", {}).get("humidity", "N/A")
        
        # Extract weather description (first weather condition)
        weather_info = weather_data.get("weather", [])
        weather_description = "N/A"
        if weather_info and len(weather_info) > 0:
            weather_description = weather_info[0].get("description", "N/A")
        
        # Display in user-friendly format (matching expected output format)
        print("\n")
        
        # Display city name only (without country code to match expected format)
        print(f"City: {city}")
        
        # Format temperature as integer if it's a number
        if isinstance(temperature, (int, float)):
            temp_display = f"{int(temperature)}°C"
        else:
            temp_display = f"{temperature}°C"
        print(f"Temperature: {temp_display}")
        
        print(f"Humidity: {humidity}%")
        
        # Capitalize first letter of weather description
        weather_display = weather_description.title() if weather_description != "N/A" else weather_description
        print(f"Weather: {weather_display}")
        print()
        
    except Exception as e:
        print(f"Error extracting weather data: {e}")


def main():
    """
    Main function to run the weather API program.
    """
    print("Weather API - Extract and Display Specific Data (Task 3)")
    print("-" * 60)
    
    # API key - Replace with your actual OpenWeatherMap API key
    # Get your free API key at: https://openweathermap.org/api
    api_key = "5b54945900fa4db64d400472c9daaea1"
    
    # Get city name from user
    city_name = input("Enter the city name: ").strip()
    
    if not city_name:
        print("Error: City name cannot be empty.")
        return
    
    # Fetch weather details
    print(f"\nFetching weather data for {city_name}...")
    weather_data = get_weather_details(city_name, api_key)
    
    # Extract and display specific weather fields in user-friendly format
    if weather_data:
        extract_and_display_weather(weather_data)
    else:
        # Error message already printed in get_weather_details function
        pass


if __name__ == "__main__":
    main()

