
# pylint: disable=too-few-public-methods
"""Modelo SQLAlchemy para la entidad Usuario."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base


class Usuario(Base):
    """Representa un usuario (niño) en BrainyKids."""
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    nivel = Column(Integer, default=1)
    puntos = Column(Integer, default=0)
    recompensas = Column(Integer, default=0)

    # Relación con tutor
    tutor_id = Column(Integer, ForeignKey("tutores.id"))

    tutor = relationship("Tutor", back_populates="usuarios")

    # Relación con progreso
    progresos = relationship("Progreso", back_populates="usuario", cascade="all, delete")
