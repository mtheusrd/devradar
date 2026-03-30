from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"🚀 {settings.app_name} v{settings.app_version} iniciando...")
    yield
    print(f"👋 {settings.app_name} encerrando...")


app = FastAPI(
    title="DevRadar API",
    description="Agregador de vagas tech",
    version="0.1.0",
    lifespan=lifespan,  
)


@app.get("/", tags=["health"])
async def root() -> dict:
    return {
        "app": "DevRadar",
        "status": "online",
        "version": "0.1.0",
    }


@app.get("/health", tags=["health"])
async def health_check() -> dict:
    return {"status": "ok"}