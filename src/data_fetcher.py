import requests

API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
BASE_URL = "https://www.alphavantage.co/query"

def fetch_stock_data(symbol, function="TIME_SERIES_DAILY"):
    params = {
        "function": function,
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()
