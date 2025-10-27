from dataclasses import dataclass
from domain.value_objects.coords import Coords

@dataclass(frozen=True)
class Place:
    name: str
    coords: Coords