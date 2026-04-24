"""Rutas de autenticación para BrainyKids."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.db import get_db
from config.security import create_access_token
from crud.crud_tutor import authenticate_tutor
from schemas.schema_auth import LoginRequest

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    """Autentica a un tutor y retorna un token JWT."""
    tutor = authenticate_tutor(db, data.email, data.password)
    if not tutor:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    token = create_access_token({
        "sub": tutor.email.lower().strip(),
        "id": tutor.id
    })
    return {
        "access_token": token,
        "token_type": "bearer"
    }
