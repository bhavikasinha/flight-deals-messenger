import os
from dotenv import load_dotenv
import requests

load_dotenv()
FLIGHT_ENDPOINT = 'https://serpapi.com/search.json'
SERPAPI_API_KEY = os.getenv("SERPAPI_APIKEY")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, cities_list):
        self.departure = os.getenv("DEPARTURE_IATA")
        self.cities = cities_list

        for city in self.cities:
            self.search_params = {
                "engine": "google_flights",
                "type": 2,
                "outbound_date": os.getenv("OUTBOUND_DATE"),
                "departure_id": self.departure,
                "arrival_id": city.iata_code,
                "currency": "INR",
                "hl": "en",
                'api_key': SERPAPI_API_KEY,
            }

            response = requests.get(url=FLIGHT_ENDPOINT, params=self.search_params)
            response.raise_for_status()
            self.search_data = response.json()

            city.cheapest_price = self.search_data["price_insights"]["lowest_price"]
