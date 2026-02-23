from fastapi import APIRouter, HTTPException

from app.core.security import create_access_token
from app.schemas.auth import LoginRequest, LoginResponse

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/login', response_model=LoginResponse)
async def login(payload: LoginRequest) -> LoginResponse:
    if payload.password != 'demo1234':
        raise HTTPException(status_code=401, detail='Invalid credentials')
    token = create_access_token(subject=payload.email)
    return LoginResponse(access_token=token)
