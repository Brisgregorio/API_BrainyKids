"""Rutas para gestión de módulos en BrainyKids."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.db import get_db
from crud.crud_modulos import get_modulos
from schemas.schema_modulos import ModuloResponse

router = APIRouter(prefix="/modulos", tags=["Modulos"])

@router.get("/", response_model=list[ModuloResponse])
def listar_modulos(db: Session = Depends(get_db)):
    """Lista todos los módulos disponibles."""
    return get_modulos(db)
