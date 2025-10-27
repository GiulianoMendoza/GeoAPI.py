import httpx
from typing import List, Optional
from domain.entities.place import Place
from domain.value_objects.coords import Coords
from application.protocols_interfaces.portsCoords import GeoReadProvider

class NominatimProvider(GeoReadProvider):
    def __init__(self, base_url: str = "https://nominatim.openstreetmap.org", user_agent: str = "geo-api-demo"):
        self.base = base_url
        self.headers = {"User-Agent": user_agent}

    def geocode(self, query: str, limit: int = 5) -> List[Place]:
        params = {"q": query, "format": "jsonv2", "limit": limit}
        r = httpx.get(f"{self.base}/search", params=params, headers=self.headers, timeout=10)
        r.raise_for_status()
        items = r.json()
        out: List[Place] = []
        for it in items:
            name = it.get("display_name") or query
            lat = float(it["lat"]); lon = float(it["lon"])
            out.append(Place(name=name, coords=Coords(lat, lon)))
        return out

    def reverse(self, coords: Coords) -> Optional[Place]:
        params = {"lat": coords.lat, "lon": coords.lon, "format": "jsonv2"}
        r = httpx.get(f"{self.base}/reverse", params=params, headers=self.headers, timeout=10)
        r.raise_for_status()
        json = r.json()
        name = json.get("display_name")
        if not name: return None
        return Place(name=name, coords=coords)
