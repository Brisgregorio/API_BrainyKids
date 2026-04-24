
# pylint: disable=too-few-public-methods
"""Esquemas Pydantic para módulos en BrainyKids."""

from typing import Optional
from pydantic import BaseModel, Field

class ModuloBase(BaseModel):  # pylint: disable=too-few-public-methods
    """Base para esquemas de módulo."""
    nombre: str = Field(min_length=2, max_length=100)
    descripcion: Optional[str] = None

class ModuloCreate(ModuloBase):  # pylint: disable=too-few-public-methods
    """Esquema para crear un módulo."""
    # No se agregan campos extra

class ModuloResponse(ModuloBase):  # pylint: disable=too-few-public-methods
    """Respuesta de módulo con ID."""
    id: int

    class Config:
        """Configuración de Pydantic para respuesta de módulo."""
        from_attributes = True

# pylint: disable=too-few-public-methods
