import sys, os
import aiohttp
import uvicorn
from fastapi import FastAPI, UploadFile
from db import TestDatabase

# from fastapi import File
# from typing import Optional
# from pydantic import BaseModel

# BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, BASE)

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     ID: int
#
# ItemList = []

# @app.get("/")
# def get_basic_info():
#     return {"message":"Welcome to our server!"}
#
# @app.post("/add_items/")
# async def create_item(item: Item):
#     ItemList.append(item)
#     return item
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     for i in ItemList:
#         if i.ID == item_id:
#             return {"message": "Item found", "item":i}
#     return {"Message": "Could not fing an item with this ID"}

app = FastAPI()

@app.post("/scan-file")
async def add_file(file: UploadFile):
    if not file:
        return "No file detected"
    else:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    'https://beta.nimbus.bitdefender.net:443/liga-ac-labs-cloud/blackbox-scanner/',
                    data={'file': await file.read()}) as resp:
                res = await resp.json()
                print(res)
                db = TestDatabase()
                await db.insert_data(res)
                print(res)
                return res

if __name__ == '__main__':
    uvicorn.run(app, port=8001)
    # uvicorn.run(app, host='0.0.0.0', port=8001)
