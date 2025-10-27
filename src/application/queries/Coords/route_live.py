from application.dto.dtoRoute import RouteOut
from application.protocols_interfaces.portsRoute import RouteProvider
from application.protocols_interfaces.portsTraffic import TrafficProvider
from domain.value_objects.coords import Coords

def handle(routeprov: RouteProvider, trafficprov: TrafficProvider,
           *, from_lat: float, from_lon: float, to_lat: float, to_lon: float,
           profile: str = "driving-car") -> RouteOut:
    o, d = Coords(from_lat, from_lon), Coords(to_lat, to_lon)
    km, mins, geom = routeprov.route(o, d, profile)
    factor = trafficprov.factor_for_route(geom)
    return RouteOut(kilometers=round(km, 2),
                    minutes=round(mins * factor, 1),
                    geometry=geom)
