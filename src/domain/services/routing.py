from typing import Dict, List, Tuple, Callable
from uuid import UUID
from domain.entities.graph import Edge

WeightFn = Callable[[Edge], float]

def dijkstra(
    start: UUID,
    goal: UUID,
    neighbors: Callable[[UUID], List[Edge]],
    weight: WeightFn
) -> Tuple[float, List[UUID]]:
    import heapq
    dist: Dict[UUID, float] = {start: 0.0}
    prev: Dict[UUID, UUID] = {}
    pq = [(0.0, start)]
    seen = set()

    while pq:
        d, u = heapq.heappop(pq)
        if u in seen: 
            continue
        seen.add(u)
        if u == goal:
            break
        for e in neighbors(u):
            v = e.to
            nd = d + weight(e)
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))

    if goal not in dist:
        return float("inf"), []
    # reconstrucción
    path = [goal]
    while path[-1] != start:
        path.append(prev[path[-1]])
    path.reverse()
    return dist[goal], path
