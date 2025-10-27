from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    pages: int
    active: Optional[bool] = True

class BookUpdate(BaseModel):
    title: str
    author: str
    pages: int
    active: bool