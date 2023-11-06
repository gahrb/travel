# Adapter for all Kiwi API calls
from kiwi_api import KiwiApi

class KiwiAdapter:
    # get all available airports
    def get_all_airports():
        return KiwiApi.get_all_airports()

    # get all available flights
    def get_all_flights(self, return_date, origin, destination):
        return KiwiApi.get_all_flights(self, return_date, origin, destination)

    # get all available airlines
    def get_all_airlines():
        return KiwiApi.get_all_airlines()