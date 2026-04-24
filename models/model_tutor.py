
# pylint: disable=too-few-public-methods
"""Modelo SQLAlchemy para la entidad Tutor."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.db import Base


class Tutor(Base):
    """Representa un tutor (adulto responsable) en BrainyKids."""
    __tablename__ = "tutores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    # Relación con usuarios (niños)
    usuarios = relationship("Usuario", back_populates="tutor")
