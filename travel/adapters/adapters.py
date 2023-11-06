
from travel.adapters.amadeus_api import get_all_airports as get_all_amadeus_airports


def populate_locations() -> List[Location]:
    # get all airports from Amadeus API
    amadeus_airports = get_all_amadeus_airports()

    # combine all airports into one list
    all_airports = kiwi_airports + skyscanner_airports + amadeus_airports

    # remove duplicates
    all_airports = list({airport.id: airport for airport in all_airports}.values())
    return all_airports


