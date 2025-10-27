from application.protocols_interfaces.portsBook import BookCommand, BookQuery
from domain.entities.book import Book
from domain.services.book_rules import ensure_unique_title
from uuid import UUID

def UpdateHandle(BookCommand: BookCommand, BookQuery: BookQuery,*,id:UUID,title:str,author:str,pages:int,active:bool)-> Book:
    current = BookQuery.get(id)
    if not current:
        raise ValueError("not found")
    if title != current.title:
        ensure_unique_title(BookQuery, title)
    _UpdateHandle = Book(id=id, title=title, author=author, pages=pages, active=active)
    BookCommand.update(_UpdateHandle)
    return _UpdateHandle