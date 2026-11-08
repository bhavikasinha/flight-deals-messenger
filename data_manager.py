import requests
import os
from dotenv import load_dotenv

load_dotenv()
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
TOKEN = os.getenv("SHEETY_TOKEN")

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=HEADERS)
        response.raise_for_status()
        self.arrival_info = response.json()['flight']
