# Práctica 3.1 – API REST con FastAPI

Autor: Ainhoa De Pablo Leal

## Descripción
API REST para la gestión de juegos de mesa.

## Creación del entorno virtual
python -m venv venv
venv\Scripts\activate

## Instalación de dependencias
pip install -r requirements.txt

## Ejecución del servidor
uvicorn main:app --reload

## Endpoints disponibles
- POST /boardgames
- GET /boardgames
- GET /boardgames/{id}
- PUT /boardgames/{id}
- DELETE /boardgames/{id}
