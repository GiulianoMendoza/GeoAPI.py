from typing import Optional, Iterable
from uuid import UUID
from domain.entities.book import Book
from ..store import STORE

class BookQuery:
    def get(self, id:UUID) -> Optional[Book]:
        return STORE.get(id)
    
    def list(self) -> Iterable[Book]:
        return list(STORE.values())
    
    def exists_title(self, title: str) -> bool:
        return any(b.title == title for b in STORE.values())