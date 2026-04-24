"""Rutas para gestión de progreso en BrainyKids."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from config.security import get_current_user
from crud.crud_progreso import (
    create_progreso, get_progreso_usuario, update_progreso, delete_progreso
)
from crud.crud_usuario import get_usuarios_by_tutor
from schemas.schema_progreso import ProgresoCreate, ProgresoResponse

router = APIRouter(prefix="/progreso", tags=["Progreso"])

@router.post("/", response_model=ProgresoResponse)
def registrar_progreso(
    progreso: ProgresoCreate,
    db: Session = Depends(get_db),
    # pylint: disable=unused-argument

    current_user=Depends(get_current_user)
):
    """Registra un nuevo progreso para un usuario en un módulo."""
    return create_progreso(
        db,
        progreso.usuario_id,
        progreso.modulo_id,
        progreso.puntaje,
    )

@router.get("/{usuario_id}", response_model=list[ProgresoResponse])
@router.get("/{usuario_id}", response_model=list[ProgresoResponse])
# pylint: disable=unused-argument
def obtener_progreso(
    usuario_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Obtiene el progreso de un usuario, validando que pertenezca al tutor autenticado."""
    usuarios = get_usuarios_by_tutor(db, current_user.id)
    if not any(u.id == usuario_id for u in usuarios):
        raise HTTPException(status_code=403, detail="No autorizado")
    return get_progreso_usuario(db, usuario_id)

@router.put("/{progreso_id}", response_model=ProgresoResponse)
def actualizar_progreso(progreso_id: int, puntaje: int, db: Session = Depends(get_db)):
    """Actualiza el puntaje de un progreso."""
    actualizado = update_progreso(db, progreso_id, puntaje)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Progreso no encontrado")
    return actualizado

@router.delete("/{progreso_id}")
def eliminar_progreso(progreso_id: int, db: Session = Depends(get_db)):
    """Elimina un progreso por su ID."""
    eliminado = delete_progreso(db, progreso_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Progreso no encontrado")
    return {"mensaje": "Progreso eliminado correctamente"}
