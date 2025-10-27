from infraestructure.repositories.bookCommand import BookCommand
from infraestructure.repositories.bookQuery import BookQuery
from infraestructure.providers.coords.nominatim import NominatimProvider
from infraestructure.providers.coords.graph_memory import MemoryGraphProvider
from infraestructure.providers.coords.traffic_free import NoTrafficProvider
import os

BookQuery = BookQuery()
BookCommand = BookCommand()
_traffic_provider = NoTrafficProvider()

def Get_BookCommand():
    return BookCommand

def Get_BookQuery():
    return BookQuery

_provider = NominatimProvider(user_agent="gimendoza-geo-api")

def get_geo_provider():
    return _provider

_graph_provider = MemoryGraphProvider()

def Get_GraphProvider():
    return _graph_provider

_route_provider = None 

def Get_RouteProvider():
    global _route_provider
    if _route_provider is None:
        api_key = os.getenv("ORS_API_KEY")
        if not api_key:
            try:
                from pathlib import Path
                env_path = Path(__file__).resolve().parents[2] / ".env"
                if env_path.exists():
                    for line in env_path.read_text(encoding="utf-8", errors="ignore").splitlines():
                        s = line.strip()
                        if not s or s.startswith("#") or "=" not in s:
                            continue
                        k, _, v = s.partition("=")
                        k = k.strip()
                        v = v.strip().strip('"').strip("'")
                        os.environ.setdefault(k, v)
                    api_key = os.getenv("ORS_API_KEY")
            except Exception:
                pass
        if not api_key:
            class _MissingKeyRouteProvider:
                def route(self, *args, **kwargs):
                    raise RuntimeError("Configurar ORS_API_KEY en variables de entorno")
            _route_provider = _MissingKeyRouteProvider()
        else:
            from infraestructure.providers.coords.openroute import ORSProvider
            _route_provider = ORSProvider(api_key=api_key)
    return _route_provider

def Get_TrafficProvider():
    return _traffic_provider
