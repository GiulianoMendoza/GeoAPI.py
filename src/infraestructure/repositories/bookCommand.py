from uuid import UUID
from domain.entities.book import Book
from ..store import STORE

class BookCommand:
    def add(self, book:Book) -> None:
        STORE[book.id] = book

    def update(self, book:Book) -> None:
        STORE[book.id] = book

    def delete(self, id:UUID) -> None:
        STORE.pop(id,None)
