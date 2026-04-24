"""Utilidades para el cálculo de nivel de usuario en BrainyKids."""

def calcular_nivel(puntos: int) -> int:
    """Calcula el nivel de usuario según sus puntos acumulados."""
    return (puntos // 100) + 1
