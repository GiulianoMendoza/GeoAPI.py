from application.protocols_interfaces.portsCoords import GeoReadProvider
from application.dto.dtoCoords import CoordsIn, ReverseOut

def CoordInHandle(provider: GeoReadProvider, dto: CoordsIn) -> ReverseOut:
    p = provider.reverse(coords= CoordIn_ToCoords(dto))
    if p:
        return ReverseOut(name=p.name, lat=p.coords.lat, lon=p.coords.lon)
    return ReverseOut(name=None, lat=dto.lat, lon=dto.lon)

def CoordIn_ToCoords(dto: CoordsIn):
    from domain.value_objects.coords import Coords
    return Coords(dto.lat, dto.lon)
