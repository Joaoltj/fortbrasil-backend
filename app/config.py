import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:061118@localhost:5432/fortbrasil")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TIME_EXPIRATION = os.getenv("TIME_EXPIRATION", 86400000)
    SECRET_KEY = os.getenv("SECRET_KEY", 'FORTBRASIL')