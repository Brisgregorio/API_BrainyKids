"""Script para crear módulos iniciales en la base de datos BrainyKids."""

from config.db import SESSION_LOCAL
from models.model_modulos import Modulo

db = SESSION_LOCAL()

modulos = [
    {"nombre": "Números", "descripcion": "Aprender números"},
    {"nombre": "Letras", "descripcion": "Aprender letras"},
    {"nombre": "Colores", "descripcion": "Aprender colores"},
    {"nombre": "Figuras", "descripcion": "Aprender figuras"},
]

for m in modulos:
    modulo = Modulo(**m)
    db.add(modulo)

db.commit()
db.close()

print("Módulos creados")
