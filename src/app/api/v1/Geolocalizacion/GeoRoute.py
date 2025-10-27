from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import Literal
from app.DependencyInjection import Get_GraphProvider,Get_RouteProvider,Get_TrafficProvider
from application.queries.Coords import route_offline as q_route
from application.queries.Coords import route_online as q_route
from application.queries.Coords import route_live  as q_live
from application.dto.dtoRoute import RouteOut
from application.UseCase.security.security import auth_guard

router = APIRouter(prefix="/v1/Geolocalizacion", tags=["Geolocalizacion"])

@router.get("/route-offline",dependencies=[Depends(auth_guard)],)
def route_offline(
    from_lat: float, from_lon: float,
    to_lat: float, to_lon: float,
    metric: Literal["time","distance"] = "time",
    provider = Depends(Get_GraphProvider)
):
    try:
        return q_route.handle(provider,from_lat=from_lat, from_lon=from_lon,to_lat=to_lat, to_lon=to_lon,metric=metric)
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))

@router.get("/route",dependencies=[Depends(auth_guard)], response_model=RouteOut)
def route(
    from_lat: float, from_lon: float,
    to_lat: float, to_lon: float,
    profile: Literal["driving-car","cycling-regular","foot-walking"] = "driving-car",
    provider = Depends(Get_RouteProvider)
):
    try:
        return q_route.handle(provider,
                              from_lat=from_lat, from_lon=from_lon,
                              to_lat=to_lat, to_lon=to_lon,
                              profile=profile)
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))
    
@router.get("/route-live",dependencies=[Depends(auth_guard)], response_model=RouteOut)
def route_live(
    from_lat: float, from_lon: float,
    to_lat: float, to_lon: float,
    profile: Literal["driving-car","cycling-regular","foot-walking"] = "driving-car",
    speed_factor: float = Query(1.0, ge=0.4, le=1.5),  
    rprov = Depends(Get_RouteProvider),
    tprov = Depends(Get_TrafficProvider),
):
    try:
        if hasattr(tprov, "fixed"):
            tprov.fixed = speed_factor
        return q_live.handle(rprov, tprov,
                              from_lat=from_lat, from_lon=from_lon,
                              to_lat=to_lat, to_lon=to_lon,
                              profile=profile)
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))