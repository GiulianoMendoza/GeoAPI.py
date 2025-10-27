from uuid import UUID
from application.protocols_interfaces.portsBook import BookQuery

def GetHandle(BookQuery: BookQuery,*, id: UUID):
    return BookQuery.get(id)
