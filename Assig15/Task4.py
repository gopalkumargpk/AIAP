import requests
import json

def get_weather_by_city(city_name):
    """
    Get weather details for a city using OpenWeatherMap API.
    (Task 4: Build a Function with Parameters)
    
    This function accepts a city name as a parameter and dynamically calls the API.
    
    Args:
        city_name (str): Name of the city to get weather for
    
    Returns:
        dict: Weather data as JSON if successful, None if error occurs
    """
    # API key - Replace with your actual OpenWeatherMap API key
    # Get your free API key at: https://openweathermap.org/api
    api_key = "5b54945900fa4db64d400472c9daaea1"
    
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
        
        # Parse JSON response
        weather_data = response.json()
        
        # Check if API returned an error in the JSON response
        if weather_data.get("cod") and str(weather_data.get("cod")) != "200":
            # City not found (404) or invalid API key (401)
            if weather_data.get("cod") == 404:
                print("Error: City not found. Please enter a valid city.")
                return None
            elif weather_data.get("cod") == 401:
                print("Error: Could not connect to API. Check your API key or network connection.")
                return None
            else:
                print("Error: City not found. Please enter a valid city.")
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
        # Handle HTTP errors
        if e.response.status_code == 404:
            print("Error: City not found. Please enter a valid city.")
        elif e.response.status_code == 401:
            print("Error: Could not connect to API. Check your API key or network connection.")
        else:
            print("Error: City not found. Please enter a valid city.")
        return None
        
    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")
        return None
        
    except json.JSONDecodeError:
        print("Error: Could not connect to API. Check your API key or network connection.")
        return None
        
    except Exception:
        print("Error: City not found. Please enter a valid city.")
        return None


def display_weather_info(weather_data):
    """
    Extract and display specific weather fields in a user-friendly format.
    
    Args:
        weather_data (dict): Weather data dictionary from API
    """
    if not weather_data:
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
        
        # Display in user-friendly format
        print()
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
    print("Weather API - Function with Parameters (Task 4)")
    print("-" * 60)
    
    # Get city name from user
    city_name = input("Enter the city name: ").strip()
    
    if not city_name:
        print("Error: City name cannot be empty.")
        return
    
    # Call the function with the city name parameter
    print(f"\nFetching weather data for {city_name}...")
    weather_data = get_weather_by_city(city_name)
    
    # Display weather information if data was retrieved successfully
    if weather_data:
        display_weather_info(weather_data)


if __name__ == "__main__":
    main()

