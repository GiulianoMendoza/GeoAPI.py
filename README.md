# 🌍 GeoAPI

**GeoAPI** es una API modular desarrollada con **FastAPI**, basada en los principios de **Clean Architecture** y **CQRS**, diseñada para resolver problemas de **geolocalización**, **rutas** y **distancias** de forma extensible y mantenible.

---

## 🚀 Objetivo

El propósito principal es ofrecer un sistema flexible y escalable que permita:

- 📍 Obtener coordenadas a partir de texto (**geocodificación**).  
- 🗺️ Obtener direcciones a partir de coordenadas (**reverse geocoding**).  
- 📏 Calcular distancias entre dos puntos.  
- ⏱️ *(Futuro)* Calcular rutas reales con tiempo estimado y trayectos mediante proveedores externos como **OpenRouteService** o **Google Maps**.  

La arquitectura está dividida en capas: **Dominio**, **Aplicación**, **Infraestructura** y **API**, garantizando bajo acoplamiento y alta testabilidad.

---

## 🧮 Tecnologías

- **Python 3.12**
- **FastAPI**
- **HTTPX**

---

## ⚙️ Instalación y Ejecución

1. Crear el entorno virtual  
   ```bash
   python -m venv fastapi-pythonenv
2. Activar el entorno
   ```bash
     .\fastapi-pythonenv\Scripts\activate
3. Instalar Dependencias:
   ```bash
     pip install fastapi uvicorn
4. Instalar Libreria httpx:
   ```bash
     pip install httpx
5. Iniciar la API:
   ```bash
     uvicorn --app-dir src app.main:app --reload
## Abrí Swagger Docs:

**http://127.0.0.1:8000/docs**

## Endpoints

| Método | Ruta                    | Descripción                                      |
| :-----: | ----------------------- | ------------------------------------------------ |
| `GET`   | `/v1/geo/geocode`       | Devuelve coordenadas a partir de un texto        |
| `GET`   | `/v1/geo/reverse`       | Devuelve dirección aproximada desde coordenadas  |
| `POST`  | `/v1/geo/distance`      | Calcula distancia entre dos puntos             |
| `GET`   | `/v1/geo/route-offline` | Calcula ruta simulada con tiempo estimado (100 km/h) |

