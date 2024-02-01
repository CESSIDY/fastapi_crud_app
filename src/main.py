from enum import Enum
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#https://github.com/zhanymkanov/fastapi-best-practices

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/with/{param}")
async def root(param: int):
    return {"message": param}

@app.post("/")
async def post():
    return {"message": "hello from the post route"}

@app.put("/")
async def put():
    return {"message": "hello from the put route"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you it good"}
    if food_name == FoodEnum.fruits:
        return {"food_name": food_name, "message": "you still good"}
    return {"food_name": food_name, "message": "daj motherfucker"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items")
async def items_list(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip+limit]

@app.get("/items/{item_id}")
async def items_list(item_id: str, q: Optional[str] = ''):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

class Item(BaseModel):
    name: str
    desc: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items")
async def read_item(item: Item):
    item_dict = item.model_dump() # dict
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
