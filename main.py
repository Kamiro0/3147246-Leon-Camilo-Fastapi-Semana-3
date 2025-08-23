from fastapi import FastAPI
from routers import products

app = FastAPI(title="API de Inventario Simple - Semana 3")

# Incluir router de productos
app.include_router(products.router)

@app.get("/")
def hello_world() -> dict:
    return {"message": "Bienvenido a la API con Pydantic!"}

@app.get("/greeting/{name}")
def greet_user(name: str) -> dict:
    return {"greeting": f"¡Hola {name}!"}

@app.get("/my-profile")
def my_profile() -> dict:
    return {
        "name": "Anderson Martinez",
        "bootcamp": "FastAPI",
        "week": 3,
        "date": "2025",
        "likes_fastapi": True
    }

@app.get("/info")
def info() -> dict:
    return {"api": "FastAPI", "week": 3, "status": "running"}

@app.get("/calculate/{num1}/{num2}")
def calculate(num1: int, num2: int) -> dict:
    result = num1 + num2
    return {"result": result, "operation": "sum"}

@app.get("/fruits")
def get_fruits() -> list[str]:
    return ["apple", "banana", "orange"]

@app.get("/numbers")
def get_numbers() -> list[int]:
    return [1, 2, 3, 4, 5]

@app.get("/user/{user_id}")
def get_user(user_id: int) -> dict:
    return {
        "id": str(user_id),
        "name": "Demo User",
        "email": "demo@example.com"
    }
