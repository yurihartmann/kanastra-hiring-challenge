from enum import Enum
from http import HTTPStatus

from pydantic import BaseModel

ContentType = str | dict | list | None
HeaderType = dict[str, str | int | float] | None


class ErrorTypeEnum(str, Enum):
    ERROR_TYPE_LOGIC = "logic"
    ERROR_TYPE_REQUEST = "request"
    ERROR_TYPE_UNKNOWN = "unknown"
    ERROR_TYPE_MISSING_DATA = "missing-data"
    ERROR_TYPE_FORBIDDEN = "forbidden"


class ApplicationExceptionSchema(BaseModel):
    status_code: int
    message: str
    content: ContentType = None
    headers: HeaderType = None
    error_type: ErrorTypeEnum


class ApplicationException(Exception):
    status_code: int
    application_exception: ApplicationExceptionSchema

    def __init__(
        self,
        message: str,
        content: ContentType = None,
        status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR,
        headers: HeaderType = None,
        error_type: ErrorTypeEnum = ErrorTypeEnum.ERROR_TYPE_UNKNOWN,
    ):
        self.status_code = status_code
        self.application_exception = ApplicationExceptionSchema(
            status_code=status_code,
            message=message,
            content=content,
            headers=headers,
            error_type=error_type,
        )

    def dump_exception(self) -> dict:
        return self.application_exception.model_dump(by_alias=True)
