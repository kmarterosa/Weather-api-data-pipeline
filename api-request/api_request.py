import requests
from creds import api_key_access

api_key = api_key_access
api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    print("Fetching weather data from API stack...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred {e}")
        raise


def mock_fetch_data():
    print("Fetching mock/fake data from API test...")
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-05-05 06:38', 'localtime_epoch': 1777963080, 'utc_offset': '-4.0'}, 'current': {'observation_time': '10:38 AM', 'temperature': 15, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'astro': {'sunrise': '05:50 AM', 'sunset': '07:57 PM', 'moonrise': 'No moonrise', 'moonset': '07:56 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 90}, 'air_quality': {'co': '212.85', 'no2': '17.95', 'o3': '111', 'so2': '8.75', 'pm2_5': '9.25', 'pm10': '9.55', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 19, 'wind_degree': 221, 'wind_dir': 'SW', 'pressure': 1011, 'precip': 0, 'humidity': 67, 'cloudcover': 0, 'feelslike': 15, 'uv_index': 0, 'visibility': 16, 'is_day': 'yes'}}


mock_fetch_data()
print(mock_fetch_data())