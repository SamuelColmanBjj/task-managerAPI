from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a SQLite (local)
SQLALCHEMY_DATABASE_URL= 'sqlite:///./tasks.db'

# Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False})

# Crear una clase base para los modelos
Base = declarative_base()

# Crear la sesión que permite interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)