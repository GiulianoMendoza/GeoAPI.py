from typing import Literal
from math import radians, sin, cos, asin, sqrt
from domain.value_objects.coords import Coords
from application.protocols_interfaces.portsRoute import GraphReadPort
from domain.services.routing import dijkstra
from shared.settings import SPEED_KMH_DEFAULT

Metric = Literal["distance", "time"]

def _haversine_km(a: Coords, b: Coords) -> float:
    r = 6371.0
    dlat = radians(b.lat - a.lat)
    dlon = radians(b.lon - a.lon)
    x = sin(dlat / 2) ** 2 + cos(radians(a.lat)) * cos(radians(b.lat)) * sin(dlon / 2) ** 2
    return 2 * r * asin(sqrt(x))

def handle(provider: GraphReadPort, *, 
           from_lat: float, from_lon: float,
           to_lat: float, to_lon: float,
           metric: Metric = "time") -> dict:
    
    o = Coords(from_lat, from_lon)
    d = Coords(to_lat, to_lon)
    s = provider.nearest_node(o)
    t = provider.nearest_node(d)

    # fallback si no hay ruta válida
    if not s or not t or s == t:
        km = _haversine_km(o, d)
        mins = (km / SPEED_KMH_DEFAULT) * 60.0
        return {
            "metric": metric,
            "total": round(mins if metric == "time" else km, 2),
            "kilometers": round(km, 2),
            "minutes": round(mins, 2),
            "path": [
                {"lat": o.lat, "lon": o.lon},
                {"lat": d.lat, "lon": d.lon},
            ],
            "note": "fallback: tiempo estimado a 100 km/h (sin ruta en grafo)"
        }

    # ruta normal dentro del grafo
    weight = (lambda e: e.time_min) if metric == "time" else (lambda e: e.distance_km)
    total, path = dijkstra(s, t, provider.neighbors, weight)
    coords_path = [provider.node(n).coords for n in path]

    km = sum(provider.neighbors(a)[[e.to for e in provider.neighbors(a)].index(b)].distance_km
             for a, b in zip(path, path[1:])) if len(path) > 1 else 0.0
    mins = sum(provider.neighbors(a)[[e.to for e in provider.neighbors(a)].index(b)].time_min
               for a, b in zip(path, path[1:])) if len(path) > 1 else 0.0

    return {
        "metric": metric,
        "total": round(total, 2),
        "kilometers": round(km, 2),
        "minutes": round(mins, 2),
        "path": [{"lat": c.lat, "lon": c.lon} for c in coords_path],
    }
