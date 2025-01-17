import requests
def fetch_weather_data(city_name):
    """
    Fetch weather data for a given city using the Open.Meteo API.
    """
    # BAse URL for the Open-Meteo API
    base_url = "https://api.open-meteo.com/v1/forecast"
    # Fake latttitude and longitude lookup for the example
    # In real applications, use a gecoding API to fetch coordinate based on the city name
    city_coordinates = {
        "New York": {"latitude": 40.7128, "longitude": -74.0060},
        "Los Angeles": {"latitude": 34.0522, "longitude": -118.2437},
        "London": {"latitude": 51.5074, "longitude": -0.1278},
        "Tokyo": {"latitude": 35.6895, "longitude":139.688},
    }
    # Check if the city exists in the pre-defined coordinates
    if city_name not in city_coordinates:
        print("Error: City not found in the coordinate list. Please add or use a gecoding API.")
        return
    # Get latitudes and longitude for the city
    coordinates = city_coordinates[city_name]
    latitude = coordinates["latitude"]
    longitude = coordinates["longitude"]
    # Parameters for the API request
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true",
    }
    try:
        # send a Get request to the  API
        response = request.get(base_url, params=params)
        response.raise_for_status() # Raise an HTTPError for bad response (4xx and 5xx)
        # Parse the JSON response
        weather_data = response.json()
        # Extract required data
        if "current_weather" in weather_data:
            current_weather = weather_data["current_weather"]
            temperature = current_weather["temperature"]
            wind_speed = current_weather["windspeed"]
            weather_desc = current_weather["weathercode"] # Weather decsription code (requires mapping)
            # Display the extracted weather details
            print(f"City: {city_name}")
            print(f"Temperature: {temperature} c")
            print(f"Weather Code: {weather_desc} (refer to API documentation for description)")
            print(f"Wind Speed: {wind_speed} km/h")
        else:
            print("Error: Unable to retrieve current weather data.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occured: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Network error: Please check your internet connection.")
    except Exception as e:
        print(f"An error occured: {e}")
# Input: Accept city name from the user
city = input("Enter the city name:")
fetch_weather_data(city)