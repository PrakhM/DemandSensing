import requests
from datetime import date, timedelta
import datetime
 
GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
 
FORECAST_HORIZON_DAYS = 14
 
 
def season_from_month(month):

    if month in (3, 4, 5, 6):
        return "Summer"
    elif month in (7, 8, 9):
        return "Monsoon"
    else:
        return "Winter"
 
 
def geocode_city(city, country_code = "IN"):
    try:
        resp = requests.get(
            GEOCODE_URL,
            params={"name": city, "count": 1, "country": country_code},
            timeout=5,
        )
        resp.raise_for_status()
        results = resp.json().get("results")
        if not results:
            return None
        return results[0]["latitude"], results[0]["longitude"]
    except (requests.RequestException, KeyError, IndexError):
        return None


def get_weather_category(city, target_date):
    fallback = season_from_month(target_date.month)

    days_out = (target_date.date() - date.today()).days
    if days_out < 0 or days_out > FORECAST_HORIZON_DAYS:
        return fallback
 
    coords = geocode_city(city)
    if coords is None:
        return fallback
 
    lat, lon = coords
    try:
        resp = requests.get(
            FORECAST_URL,
            params={
                "latitude": lat,
                "longitude": lon,
                "daily": "precipitation_sum,temperature_2m_max",
                "timezone": "auto",
                "start_date": target_date.isoformat(),
                "end_date": target_date.isoformat(),
            },
            timeout=5,
        )
        resp.raise_for_status()
        daily = resp.json().get("daily", {})
        precipitation = daily.get("precipitation_sum", [None])[0]
        max_temp = daily.get("temperature_2m_max", [None])[0]
    except (requests.RequestException, KeyError, IndexError):
        return fallback
 
    if precipitation is None or max_temp is None:
        return fallback

    if precipitation >= 10:
        return "Monsoon"
    if max_temp >= 33:
        return "Summer"
    if max_temp <= 22:
        return "Winter"
 
    return fallback
