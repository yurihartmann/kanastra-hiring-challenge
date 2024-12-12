from typing import TypeVar

from app.queue.queue_abc import QueueABC

EngineType = any
QueueReader = TypeVar("QueueReader", bound=QueueABC)
QueueWriter = TypeVar("QueueWriter", bound=QueueABC)
