from typing import Protocol, List, Optional, Tuple
from uuid import UUID
from domain.entities.graph import Node, Edge
from domain.value_objects.coords import Coords

class GraphReadPort(Protocol):
    def nearest_node(self, coords: Coords) -> Optional[UUID]: ...
    def neighbors(self, node_id: UUID) -> List[Edge]: ...
    def node(self, node_id: UUID) -> Node: ...

class RouteProvider(Protocol):
    def route(self, origin: Coords, dest: Coords, profile: str = "driving-car"
                           ) -> tuple[float, float, List[tuple[float, float]]]:
        """retorna (kilometers, minutes, geometry [ (lon,lat), ... ])"""
        ...