from application.protocols_interfaces.portsBook import BookQuery

def ListHandle(BookQuery: BookQuery):
    return list(BookQuery.list())