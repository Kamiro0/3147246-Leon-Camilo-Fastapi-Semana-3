Descripción general

Este proyecto consiste en una API REST desarrollada con FastAPI para administrar un inventario de productos.
Incluye operaciones CRUD básicas, validación de datos mediante Pydantic, manejo de errores y documentación automática con Swagger UI.

Novedades incorporadas

Se creó la carpeta routers/ para organizar los endpoints de manera más clara.

Dentro de routers/ se agregó el archivo products.py, que implementa un CRUD simple utilizando una lista en memoria.

Se añadió un models.py para centralizar los modelos de datos basados en Pydantic.

En main.py se integró el router de productos, manteniendo una estructura modular y escalable.

Se incluyó manejo de errores usando HTTPException en los endpoints.

Estructura del proyecto
estudiante-nombre/
├── main.py                 # API principal con rutas generales
├── models.py               # Modelos Pydantic (Product, etc.)
├── routers/
│   └── products.py         # CRUD de productos
├── requirements.txt        # Dependencias
└── README.md               # Documentación

Ejemplo: Endpoint POST /products

Petición (JSON):

{
  "name": "Laptop",
  "price": 2500,
  "available": true
}


Respuesta (JSON):

{
  "id": 1,
  "name": "Laptop",
  "price": 2500,
  "available": true
}

Endpoints principales

Productos

GET /products/ → Devuelve la lista completa de productos.

POST /products/ → Registra un nuevo producto.

GET /products/{product_id} → Consulta un producto por su ID.

Información general

GET / → Mensaje de bienvenida.

GET /info → Datos básicos sobre la API.

GET /my-profile → Información del desarrollador.

Dependencias necesarias

Se deben instalar las librerías indicadas en requirements.txt:

fastapi

uvicorn

pydantic

Instalación rápida:

pip install -r requirements.txt

Ejecución del servidor

Para correr la API en local:

uvicorn main:app --reload


La aplicación quedará disponible en:

http://127.0.0.1:8000

Documentación Swagger: http://127.0.0.1:8000/docs

Reflexión personal

Este trabajo me ayudó a comprender la importancia de organizar una API mediante routers para mantener el código ordenado y escalable.
Aprendí a validar datos con Pydantic y a manejar errores correctamente, lo que hace que las APIs sean más seguras y robustas.
Además, me permitió practicar la creación de endpoints REST con FastAPI, una habilidad útil para futuros proyectos más avanzados.