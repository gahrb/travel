# File containing all adapter functions for Skyscanner API

from skyscanner_api import SkyscannerApi


class SkyscannerAdapter:
    # get all available airports
    def get_all_airports():
        return SkyscannerApi.get_all_airports()

    # get all available airlines
    def get_all_airlines():
        return SkyscannerApi.get_all_airlines()

    # get all available flights
    def get_all_flights(self, return_date, origin, destination):
        return SkyscannerApi.get_all_flights(self, return_date, origin, destination)

