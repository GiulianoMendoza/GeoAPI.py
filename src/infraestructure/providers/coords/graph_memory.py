from typing import List, Optional
from uuid import UUID, uuid4
from domain.entities.graph import Node, Edge
from domain.value_objects.coords import Coords
from application.protocols_interfaces.portsRoute import GraphReadPort
from math import radians, sin, cos, asin, sqrt
from shared.settings import SPEED_KMH_DEFAULT


def haversine_km(a: Coords, b: Coords) -> float:
    r = 6371.0
    dlat = radians(b.lat - a.lat)
    dlon = radians(b.lon - a.lon)
    x = sin(dlat/2)**2 + cos(radians(a.lat))*cos(radians(b.lat))*sin(dlon/2)**2
    return 2*r*asin(sqrt(x))

class MemoryGraphProvider(GraphReadPort):
    def __init__(self):
        # nodos de ejemplo: 4 puntos entre CABA y La Plata
        self._nodes: List[Node] = [
            Node(uuid4(), Coords(-34.6037, -58.3816)),  # Obelisco
            Node(uuid4(), Coords(-34.9214, -57.9545)),  # La Plata
            Node(uuid4(), Coords(-34.7900, -58.2800)),  # nodo intermedio 1
            Node(uuid4(), Coords(-34.8600, -58.0800)),  # nodo intermedio 2
        ]
        id = [n.id for n in self._nodes]
        c  = [n.coords for n in self._nodes]

        def edge(a: int, b: int, kmh: float = SPEED_KMH_DEFAULT) -> Edge:
            km = haversine_km(c[a], c[b])
            mins = (km / kmh) * 60.0
            return Edge(to=id[b], distance_km=km, time_min=mins)

        self._adj: dict[UUID, List[Edge]] = {
            id[0]: [edge(0,2,60.0)],
            id[2]: [edge(2,0,60.0), edge(2,3,80.0)],
            id[3]: [edge(3,2,80.0), edge(3,1,80.0)],
            id[1]: [edge(1,3,80.0)],
        }

    def nearest_node(self, coords: Coords) -> Optional[UUID]:
        best = None; best_d = 1e9
        for n in self._nodes:
            d = haversine_km(coords, n.coords)
            if d < best_d:
                best, best_d = n.id, d
        return best

    def neighbors(self, node_id: UUID) -> List[Edge]:
        return self._adj.get(node_id, [])

    def node(self, node_id: UUID) -> Node:
        for n in self._nodes:
            if n.id == node_id:
                return n
        raise KeyError("node not found")
