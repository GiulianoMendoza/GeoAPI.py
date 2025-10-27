from uuid import UUID
from application.protocols_interfaces.portsBook import BookCommand, BookQuery

def DeleteHandle(BookCommand: BookCommand, BookQuery:BookQuery,*, id:UUID) -> None:
    if not BookQuery.get(id):
        raise ValueError("not found")
    BookCommand.delete(id)