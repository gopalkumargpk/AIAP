# Weather API Assignment

This project demonstrates how to connect to the OpenWeatherMap API using Python, retrieve weather data for a city, and display it in a formatted JSON output with comprehensive error handling.

## Features

- ✅ Connect to OpenWeatherMap API
- ✅ Retrieve weather data for any city
- ✅ Display formatted JSON output
- ✅ Comprehensive error handling for:
  - Network timeouts
  - Connection errors
  - Invalid API keys
  - City not found errors
  - HTTP errors
  - JSON parsing errors

## Setup Instructions

### 1. Install Required Packages

Install the `requests` library by running:

```bash
pip install requests
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

### 2. Get an API Key

1. Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api)
2. After signing up, go to your API keys section
3. Copy your API key

### 3. Configure the API Key

Open `weather_api.py` and replace `YOUR_API_KEY` on line 63 with your actual API key:

```python
api_key = "YOUR_ACTUAL_API_KEY_HERE"
```

## Usage

Run the script:

```bash
python weather_api.py
```

The program will prompt you to enter a city name, then display the weather details in JSON format.

## Example Output

```
Weather API - City Weather Details
----------------------------------------
Enter the city name: London

Fetching weather data for London...

============================================================
Weather Details (JSON Format):
============================================================
{
  "coord": {
    "lon": -0.1257,
    "lat": 51.5085
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 15.5,
    "feels_like": 14.8,
    "temp_min": 13.2,
    "temp_max": 17.1,
    "pressure": 1013,
    "humidity": 65
  },
  "visibility": 10000,
  "wind": {
    "speed": 3.5,
    "deg": 210
  },
  "clouds": {
    "all": 0
  },
  "dt": 1699123456,
  "sys": {
    "type": 2,
    "id": 2006068,
    "country": "GB",
    "sunrise": 1699087654,
    "sunset": 1699124567
  },
  "timezone": 0,
  "id": 2643743,
  "name": "London",
  "cod": 200
}
============================================================

Summary:
  City: London, GB
  Temperature: 15.5°C
  Description: Clear Sky
  Humidity: 65%
  Wind Speed: 3.5 m/s
```

## Error Handling

The script handles various error scenarios:

- **Network Timeout**: "Error: Request timed out. Please check your network connection."
- **Connection Error**: "Error: Could not connect to API. Check your network connection."
- **Invalid API Key**: "Error: Invalid API key. Please check your API key."
- **City Not Found**: "Error: City 'XYZ' not found. Please check the city name."
- **Other HTTP Errors**: Displays specific HTTP status code and error message

## API Endpoint

The script uses the OpenWeatherMap Current Weather Data API:
- Base URL: `http://api.openweathermap.org/data/2.5/weather`
- Method: GET
- Parameters: city name (`q`), API key (`appid`), units (`metric`)

## Notes

- The free tier of OpenWeatherMap API allows 60 calls per minute
- API responses are cached for a short time
- Weather data is returned in metric units (Celsius)
