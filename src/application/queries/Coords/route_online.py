from domain.value_objects.coords import Coords
from application.protocols_interfaces.portsRoute import RouteProvider
from application.dto.dtoRoute import RouteOut

def handle(provider: RouteProvider, *,
           from_lat: float, from_lon: float,
           to_lat: float, to_lon: float,
           profile: str = "driving-car") -> RouteOut:
    o = Coords(from_lat, from_lon)
    d = Coords(to_lat, to_lon)
    km, mins, geom = provider.route(o, d, profile)
    return RouteOut(kilometers=round(km, 2), minutes=round(mins, 1), geometry=geom)