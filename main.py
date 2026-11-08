#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

cities = []

data_list = data_manager.DataManager()
notif_manager = NotificationManager()

for city in data_list.arrival_info:
    iata = city['iataCode']
    arrival_city = city['city']
    price = city['lowestPrice']
    city_data = FlightData(iata_code=iata, our_price=price, city=arrival_city)
    cities.append(city_data)

flight_search = FlightSearch(cities)

for city in cities:
    if city.cheapest_price < city.our_price:
        notif_manager.send_notif(city=city)