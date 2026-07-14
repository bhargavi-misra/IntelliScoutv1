from fastapi import APIRouter

from app.api.routes.extraction import router as extraction_router

router = APIRouter()

router.include_router(extraction_router)