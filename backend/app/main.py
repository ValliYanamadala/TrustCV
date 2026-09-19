from fastapi import FastAPI
from backend.app.core.config import settings
from backend.app.api.v1.endpoints.health import router as health_router
from backend.app.api.v1.router import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# Root-level health endpoint
app.include_router(health_router)

# Versioned API routes under /api/v1
app.include_router(api_router, prefix=settings.API_V1_STR)
