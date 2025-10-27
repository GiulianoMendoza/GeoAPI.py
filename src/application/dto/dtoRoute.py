from pydantic import BaseModel
from typing import List, Tuple

class RouteOut(BaseModel):
    kilometers: float
    minutes: float
    geometry: List[Tuple[float, float]]  