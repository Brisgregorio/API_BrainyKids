
# pylint: disable=too-few-public-methods
"""Esquemas Pydantic para usuarios en BrainyKids."""

from pydantic import BaseModel, Field

class UsuarioBase(BaseModel):  # pylint: disable=too-few-public-methods
    """Base para esquemas de usuario."""
    nombre: str = Field(min_length=2, max_length=100)
    edad: int = Field(ge=3, le=6)

class UsuarioCreate(UsuarioBase):  # pylint: disable=too-few-public-methods
    """Esquema para crear usuario."""
    tutor_id: int

class UsuarioResponse(UsuarioBase):  # pylint: disable=too-few-public-methods
    """Respuesta de usuario con ID, nivel y recompensas."""
    id: int
    nivel: int
    recompensas: int

    class Config:
        """Configuración de Pydantic para respuesta de usuario."""
        from_attributes = True

# pylint: disable=too-few-public-methods
