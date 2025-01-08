from fastapi import FastAPI
from app.routes import router

app = FastAPI()

# Incluir las rutas en la aplicación
app.include_router(router)