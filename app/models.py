from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

# Definir el modelo "Task"
class Task(Base):
    __tablename__ = "tasks" # Nombre de la tabla en la base de datos


    # Definir los campos de la tabla
    id = Column(Integer, primary_key=True, index=True) # ID de la tarea, clave primaria
    title = Column(String, index=True) # Título de la tarea
    description = Column(String, nullable=True) # Descripción de la tarea (opcional)
    completed = Column(Boolean, default=False) # Estado de la tarea (completa o no)