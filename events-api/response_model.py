from pydantic import BaseModel


class BaseResponse(BaseModel):
    hash: str
    risk_level: int


class Response(BaseModel):
    file: BaseResponse
    process: BaseResponse
