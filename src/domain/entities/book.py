from dataclasses import dataclass
from uuid import UUID, uuid4

@dataclass(frozen=True)
class Book:
    id: UUID
    title: str
    author: str
    pages: int
    active: bool = True

    @staticmethod
    def create(*, title: str, author: str, pages: int) -> "Book": #el * obliga al parametro a pasar por nombre y no por posicion. 
        if not title.strip():
            raise ValueError("title required")
        if pages <= 0:
            raise ValueError("pages must be >0") #raise = throw .net
        return Book(id=uuid4(),title=title.strip(),author=author.strip(), pages=pages) #strip = trim .net