from dataclasses import dataclass
from uuid import UUID, uuid4
from domain.value_objects.coords import Coords

@dataclass(frozen=True)
class Node:
    id: UUID
    coords: Coords

@dataclass(frozen=True)
class Edge:
    to: UUID
    distance_km: float
    time_min: float
