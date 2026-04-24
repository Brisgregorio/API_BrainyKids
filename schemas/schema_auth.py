"""Esquemas Pydantic para autenticación en BrainyKids."""
from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    """Esquema para solicitud de login de tutor."""
    email: EmailStr
    password: str
