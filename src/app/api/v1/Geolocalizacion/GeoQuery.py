from fastapi import APIRouter, Depends, HTTPException, status
from application.dto.dtoCoords import GeocodeIn, GeocodeOut, CoordsIn, ReverseOut, DistanceIn
from application.queries.Coords import geocode as q_geocode, reverse as q_reverse, distance as q_dist
from app.DependencyInjection import get_geo_provider
from application.UseCase.security.security import auth_guard

router = APIRouter(prefix="/v1/Geolocalizacion", tags=["Geolocalizacion"])

@router.get("/geocode",dependencies=[Depends(auth_guard)], response_model=GeocodeOut)
def geocode(query: str, limit: int = 5, provider = Depends(get_geo_provider)):
    dto = GeocodeIn(query=query, limit=limit)
    return q_geocode.geocodeHandle(provider, dto)

@router.get("/reverse", dependencies=[Depends(auth_guard)],response_model=ReverseOut)
def reverse(lat: float, lon: float, provider = Depends(get_geo_provider)):
    dto = CoordsIn(lat=lat, lon=lon)
    try:
        return q_reverse.CoordInHandle(provider, dto)
    except ValueError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))

@router.post("/distance",dependencies=[Depends(auth_guard)])
def distance(dto: DistanceIn):
    try:
        km = q_dist.DistanceHandle(dto)
        return {"km": round(km, 3)}
    except ValueError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))
