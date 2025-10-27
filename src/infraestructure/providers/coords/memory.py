from typing import List, Optional
from domain.entities.place import Place
from domain.value_objects.coords import Coords
from application.protocols_interfaces.portsCoords import GeoReadProvider

DATA = [
    Place("Obelisco, Buenos Aires", Coords(-34.6037, -58.3816)),
    Place("Mar del Plata", Coords(-38.0055, -57.5426)),
]

class MemoryProvider(GeoReadProvider):
    def geocode(self, query: str, limit: int = 5) -> List[Place]:
        q = query.lower()
        return [p for p in DATA if q in p.name.lower()][:limit]
    def reverse(self, coords: Coords) -> Optional[Place]:
        return min(DATA, key=lambda p: p.coords.distanteKm(coords), default=None)
