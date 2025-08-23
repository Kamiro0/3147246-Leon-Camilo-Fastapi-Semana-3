Descripción General

Este proyecto implementa una API REST utilizando FastAPI para la gestión simple de productos de inventario.
Incluye un CRUD básico, validación de datos con Pydantic, manejo de errores y documentación automática con Swagger UI.

 Cosas nuevas agregadas

 Se creó la carpeta routers/ para organizar los endpoints.

 Dentro de routers/, se añadió products.py que contiene un CRUD básico para productos usando una lista en memoria.

 Se agregó un models.py para centralizar los modelos Pydantic.

 En main.py se incluyó el router de productos, manteniendo el código modular y escalable.

 Se implementó el manejo de errores con HTTPException en los endpoints.

Estructura del proyecto
estudiante-nombre/
├── main.py                 # API principal con endpoints generales
├── models.py               # Modelos Pydantic (Product, etc.)
├── routers/
│   └── products.py         # CRUD de productos
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del proyecto

▶Ejemplo de uso del endpoint POST /products

Request (body en JSON):

{
  "name": "Laptop",
  "price": 2500,
  "available": true
}


Response (ejemplo de salida):

{
  "id": 1,
  "name": "Laptop",
  "price": 2500,
  "available": true
}

Endpoints principales
Productos

GET /products/ → Lista todos los productos.

POST /products/ → Crea un nuevo producto.

GET /products/{product_id} → Obtiene un producto por ID.

Información general

GET / → Mensaje de bienvenida.

GET /info → Información básica de la API.

GET /my-profile → Datos de perfil del desarrollador.

Dependencias

El proyecto requiere instalar las dependencias listadas en requirements.txt:

fastapi
uvicorn
pydantic


Instalación rápida:

pip install -r requirements.txt

 Ejecución

Para ejecutar el servidor local:

uvicorn main:app --reload


La API estará disponible en:

http://127.0.0.1:8000

Documentación Swagger: http://127.0.0.1:8000/docs

Reflexión

Este ejercicio me permitió comprender cómo separar la lógica de la API en routers para mantener un proyecto limpio y modular.
También aprendí a utilizar Pydantic para validar datos de entrada de manera sencilla y confiable.
Ahora me siento más familiarizado con la creación de endpoints RESTful en FastAPI, lo que será útil para proyectos más complejos.