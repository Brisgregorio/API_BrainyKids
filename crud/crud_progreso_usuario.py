"""Utilidades para actualizar el progreso de usuario."""

from crud.utils import calcular_nivel

def actualizar_progreso(db, usuario, nuevos_puntos: int):
    """Actualiza el progreso y nivel de un usuario con nuevos puntos."""
    usuario.puntos += nuevos_puntos
    usuario.nivel = calcular_nivel(usuario.puntos)
    db.commit()
    db.refresh(usuario)
    return usuario
