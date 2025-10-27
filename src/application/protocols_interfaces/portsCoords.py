from typing import Protocol, List, Optional
from domain.entities.place import Place
from domain.value_objects.coords import Coords

class GeoReadProvider(Protocol):
    def geocode(self, query: str, limit: int = 5) -> List[Place]: ...
    def reverse(self, coords: Coords) -> Optional[Place]: ...