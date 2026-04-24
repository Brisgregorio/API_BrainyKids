"""Operaciones CRUD para la entidad Progreso."""

from sqlalchemy.orm import Session
from models.model_progreso import Progreso

def get_progreso_by_id(db: Session, progreso_id: int):
    """Obtiene un progreso por su ID."""
    return db.query(Progreso).filter(Progreso.id == progreso_id).first()

def update_progreso(db: Session, progreso_id: int, puntaje: int = None):
    """Actualiza el puntaje de un progreso."""
    progreso = get_progreso_by_id(db, progreso_id)
    if not progreso:
        return None
    if puntaje is not None:
        progreso.puntaje += puntaje
    db.commit()
    db.refresh(progreso)
    return progreso

def delete_progreso(db: Session, progreso_id: int):
    """Elimina un progreso por su ID."""
    progreso = get_progreso_by_id(db, progreso_id)
    if not progreso:
        return None
    db.delete(progreso)
    db.commit()
    return progreso

def create_progreso(db: Session, usuario_id: int, modulo_id: int, puntaje: int):
    """Crea un nuevo progreso para un usuario en un módulo."""
    progreso = Progreso(
        usuario_id=usuario_id,
        modulo_id=modulo_id,
        puntaje=puntaje,
    )
    db.add(progreso)
    db.commit()
    db.refresh(progreso)
    return progreso

def get_progreso_usuario(db: Session, usuario_id: int):
    """Obtiene todos los progresos de un usuario."""
    return db.query(Progreso).filter(Progreso.usuario_id == usuario_id).all()
