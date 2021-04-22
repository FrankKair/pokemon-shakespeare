from fastapi import HTTPException 


def api_error(status: int, exception: str):
    """ Raises HTTPException with status and message.

    Args:
        status: Status from FastAPI (from fastapi import status)
        message: The exception object

    Raises:
        HTTPException with given status and message derived from exception
    """
    raise HTTPException(status_code=status, detail=str(exception))
