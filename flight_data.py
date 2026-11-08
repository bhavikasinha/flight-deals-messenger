class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, iata_code, city, our_price):
        self.iata_code = iata_code
        self.city = city
        self.our_price = our_price
        self.cheapest_price : int