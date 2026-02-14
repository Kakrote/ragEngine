from fastapi import APIRouter
from app.api.routes import healthRoute
from app.api.routes import ragRoute

api_router = APIRouter()

api_router.include_router(healthRoute.router, prefix="/rag", tags=["RAG"])
api_router.include_router(ragRoute.router, prefix="/rag", tags=["RAG"])