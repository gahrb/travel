# Model file for travel app using pydantic

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, validator, Field


# Location class (representing a city/airport)
class Location(BaseModel):
    name: str
    type: str
    id: str
    code: Optional[str] = None
    country: str
    city: str
    location: str
    timezone: str
    coordinates: str
    city_id: str
    country_id: str


# Connection class (representing a flight connection)
class TravelConnection(BaseModel):
    departure: Location
    arrival: Location
    duration: int
    flight_no: str
    cost: int

# Travel class (representing a multi-stop travel option)
class Travel(BaseModel):
    stops: List[TravelConnection]
    total_duration: int
    total_cost: int
    departure_date: datetime
    return_date: datetime

    # validator to ensure that the departure date is before the return date
    @validator("return_date")
    def return_date_must_be_after_departure_date(cls, v, values):
        if "departure_date" in values and v < values["departure_date"]:
            raise ValueError("return date must be after departure date")
        return v

    # validator to ensure that the departure date is in the future
    @validator("departure_date")
    def departure_date_must_be_in_future(cls, v):
        if v < datetime.now():
            raise ValueError("departure date must be in the future")
        return v

    # validator to ensure that the return date is in the future
    @validator("return_date")
    def return_date_must_be_in_future(cls, v):
        if v < datetime.now():
            raise ValueError("return date must be in the future")
        return v


