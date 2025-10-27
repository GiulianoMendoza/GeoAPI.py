from dataclasses import dataclass
from math import radians, sin, cos, asin,sqrt

@dataclass(frozen=True)
class Coords:
    lat:float
    lon:float

    def post_init(self):
        if not (-90 <= self.lat <=90): raise ValueError("latitude out of range")
        if not (-180 <= self.lon <= 180): raise ValueError("longitude out of range")

    def distanteKm(self, other: "Coords") -> float:
        radius = 6378 
        distanceLatitude = radians(other.lat - self.lat)
        distanceLongitude = radians(other.lon - self.lon)
        angular = sin(distanceLatitude/2)**2 + cos(radians(self.lat))*cos(radians(other.lat))*sin(distanceLongitude/2)**2
        return 2 *radius *asin(sqrt(angular))