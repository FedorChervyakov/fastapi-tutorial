from typing import Optional

from fastapi import FastAPI

app = FastAPI()

fake_items = ["Foo", "Bar", "Baz"]
fake_items_db = [{"item_name": i} for i in fake_items]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
