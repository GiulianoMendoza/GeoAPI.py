from application.protocols_interfaces.portsTraffic import TrafficProvider

class NoTrafficProvider(TrafficProvider):
    def __init__(self, fixed: float = 1.0):
        self.fixed = fixed
    def factor_for_route(self, geometry):
        return self.fixed
