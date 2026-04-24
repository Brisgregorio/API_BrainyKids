"""Operaciones CRUD para la entidad Tutor."""

from sqlalchemy.orm import Session
from sqlalchemy import func
from models.model_tutor import Tutor
from config.security import hash_password, verify_password

def get_tutor_by_email(db: Session, email: str):
    """Obtiene un tutor por su email (normalizado)."""
    email_normalizado = email.strip().lower()
    print("Comparando con DB...", email_normalizado)
    return db.query(Tutor).filter(func.lower(Tutor.email) == email_normalizado).first()

def create_tutor(db: Session, nombre: str, email: str, password: str):
    """Crea un nuevo tutor si el email no está registrado."""
    existente = get_tutor_by_email(db, email)
    if existente:
        raise ValueError("El email ya está registrado")
    hashed_password = hash_password(password)
    nuevo = Tutor(
        nombre=nombre,
        email=email,
        password=hashed_password
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def authenticate_tutor(db: Session, email: str, password: str):
    """Autentica un tutor por email y contraseña."""
    tutor = get_tutor_by_email(db, email)
    if not tutor:
        return None
    if not verify_password(password, tutor.password):
        return None
    return tutor
