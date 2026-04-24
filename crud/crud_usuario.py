"""Operaciones CRUD para la entidad Usuario."""

from sqlalchemy.orm import Session
from models.model_usuario import Usuario
def delete_usuario(db: Session, usuario_id: int):
    """Elimina un usuario por su ID."""
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        return None
    db.delete(usuario)
    db.commit()
    return usuario

def get_usuario_por_correo(db: Session, correo: str):
    """Obtiene un usuario por su correo electrónico."""
    return db.query(Usuario).filter(Usuario.email == correo).first()

def create_usuario(db: Session, nombre: str, edad: int, tutor_id: int):
    """Crea un nuevo usuario."""
    usuario = Usuario(
        nombre=nombre,
        edad=edad,
        tutor_id=tutor_id,
        puntos=0,
        nivel=1
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def get_usuarios_by_tutor(db: Session, tutor_id: int):
    """Obtiene todos los usuarios asociados a un tutor."""
    return db.query(Usuario).filter(Usuario.tutor_id == tutor_id).all()
