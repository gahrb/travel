# Functions to interact with Amadeus API

from amadeus import Client, ResponseError

# set up Amadeus API

amadeus = Client(
    client_id="",
    client_secret="",
    log_level="debug",
    hostname="production",
)

# get all available airports
def load_all_airports():
    try:
        response = amadeus.reference_data.locations.get(
            keyword="",
            subType=Client.AIRPORT,
        )
        return response.data
    except ResponseError as error:
        print(error)

# get all available airlines
def load_all_airlines():
    try:
        response = amadeus.reference_data.airlines.get()
        return response.data
    except ResponseError as error:
        print(error)

# get all available flights
def load_all_flights(departure_date, return_date, origin, destination):
    try:
        response = amadeus.shopping.flight_offers.get(
            originLocationCode="",
            destinationLocationCode="",
            departureDate="",
            adults=1,
            max=250,
        )
        return response.data
    except ResponseError as error:
        print(error)
