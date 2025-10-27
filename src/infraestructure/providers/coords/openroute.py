import os, httpx
from typing import List, Tuple
from domain.value_objects.coords import Coords
from application.protocols_interfaces.portsRoute import RouteProvider

class ORSProvider(RouteProvider):
    def __init__(self, base: str = "https://api.openrouteservice.org/v2/directions", api_key: str | None = None):
        self.base = base
        self.key = api_key or os.getenv("ORS_API_KEY")
        if not self.key:
            raise RuntimeError("Configurar ORS_API_KEY en variables de entorno")
        self.headers = {"Authorization": self.key}

    def route(self, origin: Coords, dest: Coords, profile: str = "driving-car"
             ) -> tuple[float, float, List[tuple[float, float]]]:
        url = f"{self.base}/{profile}"
        params = {"start": f"{origin.lon},{origin.lat}", "end": f"{dest.lon},{dest.lat}"}
        r = httpx.get(url, params=params, headers=self.headers, timeout=15)
        r.raise_for_status()
        j = r.json()
        feat = j["features"][0]
        s = feat["properties"]["summary"]
        meters = float(s["distance"])
        seconds = float(s["duration"])
        coords = feat["geometry"]["coordinates"]   
        km = meters / 1000.0
        mins = seconds / 60.0
        geometry: List[tuple[float, float]] = [(float(lon), float(lat)) for lon, lat in coords]
        return km, mins, geometry