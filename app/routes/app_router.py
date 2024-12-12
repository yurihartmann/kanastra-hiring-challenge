from fastapi import APIRouter

from app.routes.v1.v1_router import v1_router

app_router = APIRouter()

app_router.include_router(router=v1_router)
