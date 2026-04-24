"""Rutas para gestión de tutores en BrainyKids."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from crud.crud_tutor import create_tutor
from schemas.schema_tutor import TutorCreate, TutorResponse

router = APIRouter(prefix="/tutores", tags=["Tutores"])

@router.post("/", response_model=TutorResponse)
def registrar_tutor(tutor: TutorCreate, db: Session = Depends(get_db)):
    """Registra un nuevo tutor."""
    try:
        return create_tutor(db, tutor.nombre, tutor.email, tutor.password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
