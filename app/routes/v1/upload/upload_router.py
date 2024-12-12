from datetime import datetime
from http import HTTPStatus

from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
from dishka.integrations.fastapi import DishkaRoute, FromDishka

from app.services.v1.file_processor.file_processor_service import FileProcessorService

weather_router = APIRouter(prefix='/upload', route_class=DishkaRoute)


@weather_router.post(
    path='/',
    status_code=HTTPStatus.OK,
)
async def process_file(
    file: UploadFile,
    file_processor_service: FromDishka[FileProcessorService],
):
    start = datetime.now()
    await file_processor_service.process_uploaded_file(file=file)
    return JSONResponse(content={
        "success": True,
        "time_in_seconds": (datetime.now() - start).seconds
    })
