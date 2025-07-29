# src/api/v1/endpoints/health.py
from fastapi import APIRouter
from src.utils.logger import logger

router = APIRouter()

@router.get("/health", summary="Health check endpoint", response_description="API health status")
async def health_check():
    logger.info("Health check endpoint called.")
    return {"status": "ok", "message": "SQL AI Agent API is running!"}