# pylint: disable=too-few-public-methods
"""Esquemas Pydantic para tutores en BrainyKids."""
from pydantic import BaseModel, EmailStr, Field

class TutorBase(BaseModel):  # pylint: disable=too-few-public-methods
    """Base para esquemas de tutor."""
    nombre: str = Field(min_length=2, max_length=100)
    email: EmailStr

class TutorCreate(TutorBase):  # pylint: disable=too-few-public-methods
    """Esquema para crear tutor."""
    password: str = Field(min_length=6, max_length=72)

class TutorResponse(TutorBase):  # pylint: disable=too-few-public-methods
    """Respuesta de tutor con ID."""
    id: int

    class Config:
        """Configuración de Pydantic para respuesta de tutor."""
        from_attributes = True

# pylint: disable=too-few-public-methods
