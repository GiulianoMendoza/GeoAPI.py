from fastapi import FastAPI
from pathlib import Path

# Carga variables desde .env en el root del proyecto
try:
    from dotenv import load_dotenv  # type: ignore
    project_root = Path(__file__).resolve().parents[2]
    load_dotenv(project_root / ".env")
except Exception:
    # Si python-dotenv no está instalado, simplemente continúa;
    # las variables deberán venir del entorno del sistema/Docker.
    pass
from app.api.v1.Book.bookCommand import router as cmd_router
from app.api.v1.Book.bookQuery import router as qry_router
from app.api.v1.Geolocalizacion.GeoQuery import router as geo_router  
from app.api.v1.Geolocalizacion.GeoRoute import router as route_offline_router
from app.api.v1.User.auth import router as auth_router


app = FastAPI()
app.include_router(cmd_router)
app.include_router(qry_router)
app.include_router(geo_router)  
app.include_router(route_offline_router) 
app.include_router(auth_router) 

@app.get("/", include_in_schema=False)
def health():
    return {"status": "ok"}
