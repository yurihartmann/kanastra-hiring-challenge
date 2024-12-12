from fastapi import UploadFile

from app.constants import QueueWriter


class FileProcessorService:

    def __init__(
            self,
            queue: QueueWriter
    ):
        self.queue = queue

    def __read_file(self, file: UploadFile) -> list[str]:
        file.file.readline()
        for line in file.file.readlines():
            yield line.decode().strip()

    async def process_uploaded_file(self, file: UploadFile):
        for line in self.__read_file(file):
            self.queue.put(line)
