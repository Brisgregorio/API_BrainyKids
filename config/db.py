"""Establece la conexión con la base de datos para BrainyKids."""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv(
    "SQLALCHEMY_DATABASE_URL",
    "mysql+pymysql://root:1234@localhost:3306/base_brainykids",
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SESSION_LOCAL = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def init_db():
    """Crea las tablas automáticamente."""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Provee una sesión de base de datos y la cierra al finalizar."""
    db = SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()
