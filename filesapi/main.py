import sys, os
import aiohttp
import uvicorn
from fastapi import FastAPI, UploadFile
from db import TestDatabase
from fastapi import HTTPException


app = FastAPI()


@app.post("/scan-file")
async def add_file(file: UploadFile):
    if not file:
        return "No file detected"
    else:
        file_bytes = await file.read()
        if file_bytes[:2] == b"MZ":
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    "https://beta.nimbus.bitdefender.net:443/liga-ac-labs-cloud/blackbox-scanner/",
                    data={"file": file_bytes},
                ) as resp:

                    if resp.status == 200:
                        res = await resp.json()
                        print(res)
                        db = TestDatabase()
                        await db.insert_data(res)
                        print(res)
                        return res
                    else:
                        raise HTTPException(status_code=400, detail=resp.reason)
        else:
            raise HTTPException(status_code=400, detail="Not an exec windows file")


if __name__ == "__main__":
    # uvicorn.run(app, port=8001)
    uvicorn.run(app, host="0.0.0.0", port=8001)
