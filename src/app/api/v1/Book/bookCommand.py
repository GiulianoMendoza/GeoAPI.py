from fastapi import APIRouter, Depends, HTTPException, status
from application.dto.dtoBook import BookCreate, BookUpdate
from application.commands import create_book, update_book, delete_book
from app.DependencyInjection import Get_BookCommand, Get_BookQuery
from uuid import UUID

router = APIRouter(prefix="/v1/books", tags=["Books"])

@router.post("", status_code=status.HTTP_201_CREATED)
def Create(dto: BookCreate,_bookquery = Depends(Get_BookQuery), _bookcommand = Depends(Get_BookCommand)):
    try:
        return create_book.CreateHandle(_bookcommand,_bookquery,**dto.model_dump())
    except ValueError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))

@router.put("/{id}", status_code=status.HTTP_200_OK)    
def Update(id:UUID,dto:BookUpdate, _bookquery = Depends(Get_BookQuery), _bookcommand = Depends(Get_BookCommand)):
    try:
        return update_book.UpdateHandle(_bookcommand,_bookquery,id=id,**dto.model_dump())
    except ValueError as e:
        code = status.HTTP_404_NOT_FOUND if "not found" in str(e) else status.HTTP_400_BAD_REQUEST
        raise HTTPException(code, str(e))

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def Delete(id:UUID, _bookquery = Depends(Get_BookQuery), _bookcommand = Depends(Get_BookCommand)):
    try: 
        delete_book.DeleteHandle(_bookcommand,_bookquery,id=id)
    except ValueError:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "not found")