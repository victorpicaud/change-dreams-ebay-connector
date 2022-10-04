from typing import Union


from fastapi import FastAPI
from pydantic import BaseModel

class TradableItem(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/find/item/singlematch")
def find_single_item_matches(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/find/item/singlematch")
def find_multiple_items_matches(item_id: int, q: Union[str, None] = None):
    return "Not Implemented"




class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
