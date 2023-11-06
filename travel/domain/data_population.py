# Function to populate the data classes with data from the apis

import requests
import pandas as pd
import numpy as np

from travel.models.travel import Travel, TravelConnection, Location
from travel.adapters.kiwi import KiwiAdapter

def populate_locations() -> List[Location]:

