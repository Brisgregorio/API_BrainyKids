"""Rutas para gestión de usuarios en BrainyKids."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from config.security import get_current_user
from crud.crud_usuario import create_usuario, get_usuarios_by_tutor, delete_usuario
from models.model_usuario import Usuario
from schemas.schema_usuario import UsuarioCreate, UsuarioResponse

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Elimina un usuario por su ID."""
    usuario = delete_usuario(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado correctamente"}

@router.put("/{usuario_id}/recompensas", response_model=UsuarioResponse)
def sumar_recompensas(usuario_id: int, recompensas: int, db: Session = Depends(get_db)):
    """Suma recompensas a un usuario."""
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario.recompensas += recompensas
    db.commit()
    db.refresh(usuario)
    return usuario

@router.post("/", response_model=UsuarioResponse)
def crear_usuario(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Crea un nuevo usuario asociado al tutor autenticado."""
    return create_usuario(db, usuario.nombre, usuario.edad, current_user.id)

@router.get("/", response_model=list[UsuarioResponse])
def obtener_usuarios(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Obtiene todos los usuarios asociados al tutor autenticado."""
    return get_usuarios_by_tutor(db, current_user.id)
