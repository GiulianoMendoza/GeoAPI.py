from pydantic import BaseModel, Field
from typing import List, Optional

class GeocodeIn(BaseModel):
    query: str = Field(min_length=2)
    limit: int = 5

class CoordsIn(BaseModel):
    lat: float
    lon: float

class PlaceOut(BaseModel):
    name: str
    lat: float
    lon: float

class GeocodeOut(BaseModel):
    results: List[PlaceOut]

class ReverseOut(BaseModel):
    name: Optional[str]
    lat: float
    lon: float

class DistanceIn(BaseModel):
    from_: CoordsIn
    to: CoordsIn
