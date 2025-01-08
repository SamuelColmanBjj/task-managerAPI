from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Task
from app.database import SessionLocal, Base, engine


# Crear la tabla si no existe
Base.metadata.create_all(bind=engine)


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Ruta para agregar una tarea
@router.post("/tasks/")
def create_task(title:str, description:str = None, db: Session = Depends(get_db)):
    db_task = Task(title=title, description = description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Ruta para obtener todas las tareas
@router.get("/tasks/")
def get_tasks(db:Session = Depends(get_db)):
    tasks = db.query(Task).all()  # Obtener todas las tareas de la base de datos
    return tasks   # Devolver las tareas

# Ruta para obtener una tarea por ID
@router.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first() # Buscar tarea por ID
    if task is None:
        raise HTTPException(status_code=404, detail="Task no found") # Si no se encuentra la tarea, lanzar error 404
    return task # Devolver Tarea

# Ruta para actualizar una tarea
@router.put("/tasks/{task_id}")
def update_task(task_id: int, title:str, description: str = None, 
db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first() # Buscar tarea por ID
    if task is None:
        raise HTTPException(status_code=404, detail="Task no found") # Si no se encuentra, lanzar error 404
    
    task.title = title   # Actualizar el título
    task.description = description   # Actualizar la descripción
    db.commit()   # Guardar los cambios en la base de datos
    db.refresh(task)   # Refrescar la instancia de la tarea
    return task   # Devolver la tarea actualizada

# Ruta para eliminar una tarea
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first() # Buscar tarea por ID
    if task is None:
        raise HTTPException(status_code=404, detail="Task no found")  # Si no se encuentra, lanzar error 404
    
    db.delete(task)  # Eliminar la tarea de la base de datos
    db.commit()   # Confirmar la eliminación
    return {"message": "Task deleted successfully"}  # Devolver mensaje de éxito
