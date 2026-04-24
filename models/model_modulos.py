
# pylint: disable=too-few-public-methods
"""Modelo SQLAlchemy para la entidad Modulo."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.db import Base


class Modulo(Base):
    """Representa un módulo de aprendizaje en BrainyKids."""
    __tablename__ = "modulos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255))

    progresos = relationship("Progreso", back_populates="modulo")
