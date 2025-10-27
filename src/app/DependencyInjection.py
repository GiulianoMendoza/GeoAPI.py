from infraestructure.repositories.bookCommand import BookCommand
from infraestructure.repositories.bookQuery import BookQuery
from infraestructure.providers.coords.nominatim import NominatimProvider
from infraestructure.providers.coords.graph_memory import MemoryGraphProvider
from infraestructure.providers.coords.openroute import ORSProvider
from infraestructure.providers.coords.traffic_free import NoTrafficProvider

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
_route_provider = ORSProvider()  

def Get_RouteProvider():
    return _route_provider

def Get_RouteProvider():   return _route_provider
def Get_TrafficProvider(): return _traffic_provider