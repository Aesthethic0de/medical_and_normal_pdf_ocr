from random import randint
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class Available_Cuisine(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"

food_items = {
    'indian' : ['samosa', 'Dosa'],
    'american' : ['hot dog', 'apple pie'],
    'italian' : ['pasta', 'pizza', 'sandwich']
}

valid_cuisines = food_items.keys()

@app.get("/get_items/{cuisine}")

async def get_items(cuisine : Available_Cuisine):

    return food_items.get(cuisine)

coupon_code ={
    1 : "you get 10% discount",
    2 : "you get 20% discount",
    3 : "you get 30% discount"
}

@app.get("/coupon_codes/{code}")

async def coupon(code : int):

    return {"discount" : coupon_code.get(code)}
