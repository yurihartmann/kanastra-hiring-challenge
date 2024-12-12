from tempfile import TemporaryFile
from unittest.mock import Mock
from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest
import pytest_asyncio
from httpx._types import RequestFiles
from dishka import Provider, Scope, provide, make_async_container
from dishka.integrations.fastapi import setup_dishka

from app.constants import QueueWriter
from app.routes.app_router import app_router
from app.services.v1.file_processor.file_processor_service import FileProcessorService


class ProviderTest(Provider):
    @provide(scope=Scope.APP)
    def queue_writer(self) -> QueueWriter:
        return Mock()

    fps = provide(FileProcessorService, scope=Scope.REQUEST)


@pytest_asyncio.fixture
async def container():
    container = make_async_container(ProviderTest())
    yield container
    await container.close()


@pytest.fixture
def client(container):
    app = FastAPI()
    app.include_router(router=app_router)
    setup_dishka(container, app)
    with TestClient(app) as client:
        yield client

@pytest_asyncio.fixture
async def queue_mock(container):
    return await container.get(QueueWriter)


@pytest.mark.asyncio
async def test_upload(client: TestClient, queue_mock: Mock):
    # Arrange
    tp = TemporaryFile()
    tp.write("Dennis Davis,7479,angela12@example.com,9269,2022-10-23,a65abc5f-4760-42a5-9dc3-a68526e48a5f".encode())

    _files = {'file': open(tp.name, "rb")}

    # Act
    response = client.post("/v1/upload", files=_files)

    # Assert
    assert response.status_code == 200