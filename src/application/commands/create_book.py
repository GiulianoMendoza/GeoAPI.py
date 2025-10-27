from application.protocols_interfaces.portsBook import BookCommand, BookQuery
from domain.entities.book import Book
from domain.services.book_rules import ensure_unique_title

def CreateHandle(BookCommand: BookCommand, BookQuery: BookQuery,*, title:str, author:str,pages: int, active:bool=True) ->Book:
    ensure_unique_title(BookQuery,title)
    book = Book.create(title=title,author=author, pages=pages)
    if book.active != active:
        book = Book(id=book.id, title=book.title, author=book.author, pages=book.pages, active=book.active)
    BookCommand.add(book)
    return book