# src/api/v1/api.py
from fastapi import APIRouter
from src.api.v1.endpoints import sql_chat, health

api_router = APIRouter()

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(sql_chat.router, prefix="/sql-agent", tags=["SQL Agent"])