from fastapi import APIRouter, HTTPException, status
from application.UseCase.security.auth_service import login

router = APIRouter(prefix="/v1/auth", tags=["Auth"])

@router.post("/login")
def login_user(username: str, password: str):
    try:
        token = login(username, password)
        return {"access_token": token, "token_type": "bearer"}
    except ValueError as e:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, str(e))
