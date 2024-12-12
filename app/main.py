import threading
from http import HTTPStatus

from fastapi import FastAPI
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from pydantic import ValidationError
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlmodel import SQLModel

from app.constants import EngineType
from app.exceptions.application_exception import ApplicationException
from app.providers.app_providers import ServicesProvider
from app.routes.app_router import app_router
from app.tasks.file_processor_task import FileProcessorTask

app = FastAPI()
app.include_router(router=app_router)

container = make_async_container(ServicesProvider())
setup_dishka(container, app)


@app.on_event("startup")
async def startup_event():
    engine = await container.get(EngineType)
    SQLModel.metadata.create_all(engine)

    fps = await container.get(FileProcessorTask)
    threading.Thread(target=fps.start_consume_lines).start()


@app.exception_handler(ApplicationException)
async def application_exception_handler(_, exc: ApplicationException):
    return JSONResponse(content=exc.dump_exception(), status_code=exc.status_code)


@app.exception_handler(ValidationError)
async def validation_error_handler(_, exc: ValidationError):
    return JSONResponse(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content={"detail": jsonable_encoder(exc.errors())},
    )