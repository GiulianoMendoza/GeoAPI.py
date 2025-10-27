from application.dto.dtoCoords import DistanceIn
from domain.value_objects.coords import Coords

def DistanceHandle(dto: DistanceIn) -> float:
    distanciaA = Coords(dto.from_.lat, dto.from_.lon)
    distanciaB = Coords(dto.to.lat, dto.to.lon)
    return distanciaA.distanteKm(distanciaB)
