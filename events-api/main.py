import sys, os
import aioredis

from prometheus_fastapi_instrumentator import Instrumentator

from filesapi.db import TestDatabase
from event_model import Event
from response_model import Response, BaseResponse
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {'title': 'FastFile System'}

@app.post("/events", response_model=Response)
async def add_event(event: Event) -> Response:
    r = -1
    # redis cache logic
    redis = aioredis.from_url("redis://localhost")

    value = await redis.get(event.file.file_hash)
    if value is not None:
        print("Found in cache")
        r = value.decode("utf-8")

    # mongodb
    else:
        db = TestDatabase()
        risk = await db.find_data(some_key=event.file.file_hash)

        # scan file api
        if risk is not None:
            r = risk['risk_level']
            await redis.set(event.file.file_hash, f"{r}")
            await redis.expire(event.file.file_hash, 25)
            print("Found in database")

    await redis.close()

    return Response(file=BaseResponse(hash=event.file.file_hash, risk_level=r),
                    process=BaseResponse(hash=event.last_access.hash, risk_level=r))

Instrumentator().instrument(app).expose(app)
if __name__ == '__main__':
    # uvicorn.run(app, port=8000)
    uvicorn.run(app, host="0.0.0.0", port=8000)