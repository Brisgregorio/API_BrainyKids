"""Punto de entrada principal para la API de BrainyKids."""

from fastapi import FastAPI
from config.db import init_db

from routes import (
    routes_auth,
    routes_tutor,
    routes_usuario,
    routes_modulos,
    routes_progreso
)

app = FastAPI()

init_db()

app.include_router(routes_auth.router)
app.include_router(routes_tutor.router)
app.include_router(routes_usuario.router)
app.include_router(routes_modulos.router)
app.include_router(routes_progreso.router)

@app.get("/")
def root():
    """Endpoint raíz para verificar el estado de la API."""
    return {"mensaje": "API BrainyKids funcionando "}
