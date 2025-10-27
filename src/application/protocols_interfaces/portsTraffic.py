from typing import Protocol, List, Tuple

class TrafficProvider(Protocol):
    def factor_for_route(self, geometry: list[tuple[float, float]]) -> float:
        """Devuelve factor [0.4..1.2] para ajustar minutos. 1.0 = sin tráfico."""
        ...