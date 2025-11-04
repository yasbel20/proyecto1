from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="Mi API con FastAPI",
    description="Ejemplo de FastAPI más avanzado con parámetros y rutas dinámicas",
    version="1.0.0"
)

# Ruta simple
@app.get("/ping")
def ping():
    return {"message": "pong"}

# Ruta principal
@app.get("/")
def hola_mundo():
    return {"message": "¡Hola mundo!"}

# Ruta con parámetro de ruta
@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"message": f"¡Hola, {nombre}!"}

# Ruta con parámetros opcionales de consulta
@app.get("/suma")
def suma(a: int, b: int = 0):
    """Suma dos números. `b` es opcional y por defecto 0"""
    return {"resultado": a + b}

# Ruta que lanza un error si no encuentra algo
usuarios = {"1": "Alice", "2": "Bob"}
@app.get("/usuario/{user_id}")
def obtener_usuario(user_id: str):
    if user_id in usuarios:
        return {"user_id": user_id, "nombre": usuarios[user_id]}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
