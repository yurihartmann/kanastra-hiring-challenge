from http import HTTPStatus

from app.exceptions.application_exception import ApplicationException, ErrorTypeEnum


class FileWrongException(ApplicationException):
    def __init__(self, ex: Exception):
        super().__init__(
            message=f"Line with error: {ex}",
            content="File do not match schema",
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            error_type=ErrorTypeEnum.ERROR_TYPE_MISSING_DATA,
        )
