import asyncio

import dotenv

from app.providers.app_providers import ServicesProvider

from dishka import make_async_container

from app.tasks.file_processor_task import FileProcessorTask

container = make_async_container(ServicesProvider())

async def main():
    fps = await container.get(FileProcessorTask)
    fps.start_consume_lines()


dotenv.load_dotenv()
asyncio.run(main())
