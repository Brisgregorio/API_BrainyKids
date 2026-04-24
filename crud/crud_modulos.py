"""Operaciones CRUD para la entidad Modulo."""

from sqlalchemy.orm import Session
from models.model_modulos import Modulo

def get_modulo_by_id(db: Session, modulo_id: int):
    """Obtiene un módulo por su ID."""
    return db.query(Modulo).filter(Modulo.id == modulo_id).first()

def update_modulo(db: Session, modulo_id: int, nombre: str = None, descripcion: str = None):
    """Actualiza los datos de un módulo existente."""
    modulo = get_modulo_by_id(db, modulo_id)
    if not modulo:
        return None
    if nombre is not None:
        modulo.nombre = nombre
    if descripcion is not None:
        modulo.descripcion = descripcion
    db.commit()
    db.refresh(modulo)
    return modulo

def delete_modulo(db: Session, modulo_id: int):
    """Elimina un módulo por su ID."""
    modulo = get_modulo_by_id(db, modulo_id)
    if not modulo:
        return None
    db.delete(modulo)
    db.commit()
    return modulo

def get_modulos(db: Session):
    """Obtiene todos los módulos."""
    return db.query(Modulo).all()

def create_modulo(db: Session, nombre: str, descripcion: str):
    """Crea un nuevo módulo."""
    modulo = Modulo(nombre=nombre, descripcion=descripcion)
    db.add(modulo)
    db.commit()
    db.refresh(modulo)
    return modulo
