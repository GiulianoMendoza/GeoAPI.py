from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from app.DependencyInjection import Get_BookQuery
from application.queries import get_book, list_book

router = APIRouter(prefix="/v1/books", tags=["Books"])

@router.get("")
def list_all(_bookQuery = Depends(Get_BookQuery)):
    return list_book.ListHandle(_bookQuery)

@router.get("/{id}")
def by_id(id: UUID, _bookQuery = Depends(Get_BookQuery)):
    b = get_book.GetHandle(_bookQuery, id=id)
    if not b:
        raise HTTPException(404, "not found")
    return b
