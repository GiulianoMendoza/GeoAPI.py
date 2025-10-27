from application.protocols_interfaces.portsCoords import GeoReadProvider
from application.dto.dtoCoords import GeocodeIn, GeocodeOut, PlaceOut

def geocodeHandle(provider: GeoReadProvider, dto: GeocodeIn) -> GeocodeOut:
    places = provider.geocode(dto.query, dto.limit)
    return GeocodeOut(results=[PlaceOut(name=p.name, lat=p.coords.lat, lon=p.coords.lon) for p in places])
