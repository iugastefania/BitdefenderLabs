from pydantic import BaseModel


class Device(BaseModel):
    id: str
    os: str


class LastAccess(BaseModel):
    hash: str
    path: str
    pid: str


class Time(BaseModel):
    a: int
    m: int


class File(BaseModel):
    file_hash: str
    file_path: str
    time: Time


class Event(BaseModel):
    device: Device
    file: File
    last_access: LastAccess
