# pylint: disable=too-few-public-methods
"""Esquemas Pydantic para progreso en BrainyKids."""
from pydantic import BaseModel, Field


class ProgresoBase(BaseModel):  # pylint: disable=too-few-public-methods
    """Base para esquemas de progreso."""
    usuario_id: int
    modulo_id: int
    puntaje: int = Field(ge=0, le=100)

class ProgresoCreate(ProgresoBase):  # pylint: disable=too-few-public-methods
    """Esquema para crear progreso."""
    # No se agregan campos extra

class ProgresoResponse(ProgresoBase):  # pylint: disable=too-few-public-methods
    """Respuesta de progreso con ID."""
    id: int

    class Config:
        """Configuración de Pydantic para respuesta de progreso."""
        from_attributes = True

# pylint: disable=too-few-public-methods
