
# pylint: disable=too-few-public-methods
"""Modelo SQLAlchemy para la entidad Progreso."""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base


class Progreso(Base):
    """Representa el progreso de un usuario en un módulo."""
    __tablename__ = "progreso"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"))
    modulo_id = Column(Integer, ForeignKey("modulos.id"))

    puntaje = Column(Integer)
    nivel = Column(Integer)

    usuario = relationship("Usuario", back_populates="progresos")
    modulo = relationship("Modulo", back_populates="progresos")
