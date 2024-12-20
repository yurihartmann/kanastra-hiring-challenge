from fastapi import APIRouter

from app.routes.v1.upload.upload_router import upload_router

v1_router = APIRouter(prefix='/v1')


v1_router.include_router(router=upload_router)
