import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:061118@localhost:5432/fortbrasil")
    SQLALCHEMY_TRACK_MODIFICATIONS = True