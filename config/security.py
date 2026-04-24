"""Funciones de seguridad y autenticación para BrainyKids."""


import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models.model_tutor import Tutor

import config.db

load_dotenv()

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY") or "brainykids-dev-secret"
ALGORITHM = os.getenv("ALGORITHM") or "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES") or 60)
BEARER_SCHEME = HTTPBearer()

def hash_password(password: str) -> str:
    """Genera el hash de una contraseña."""
    return PWD_CONTEXT.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica una contraseña contra su hash."""
    return PWD_CONTEXT.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Genera un token JWT con expiración."""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_db():
    """Provee una sesión de base de datos y la cierra al finalizar."""
    db = config.db.SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(BEARER_SCHEME),
    db: Session = Depends(get_db),
):
    """Obtiene el tutor autenticado a partir del token JWT."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido o expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("TOKEN RECIBIDO:", token)
        print("PAYLOAD:", payload)
        correo: str | None = payload.get("sub")
        if correo is None:
            raise credentials_exception
        correo = correo.lower().strip()
        print("Correo token:", correo)
    except JWTError as e:
        print("ERROR JWT:", e)
        raise credentials_exception from e
    tutor = db.query(Tutor).filter(Tutor.email == correo).first()
    print("Tutor encontrado:", tutor)
    if tutor is None:
        raise HTTPException(status_code=401, detail="Tutor no encontrado")
    return tutor
