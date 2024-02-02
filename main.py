import os

from typing import Optional, List
from datetime import datetime
from typing import Annotated
from fastapi import FastAPI, Body, HTTPException, status
import motor.motor_asyncio
from pydantic import ConfigDict, BaseModel, Field, EmailStr
from pydantic import BaseModel, BeforeValidator
from fastapi_pagination import Page,Params
from models import Product , Order , ProductCollection , OrderCollection

## Connection to mongo 
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://Kiranpreet:Kiran13@cluster0.wzcakcy.mongodb.net/?retryWrites=true&w=majority") ## env.variable ..... TODO

db = client.get_database("Ecom_web_database")
product_collection = db.get_collection("Product")
order_collection = db.get_collection("Order")



app = FastAPI()


@app.post("/products/",
          response_description="Add new product",
        response_model=Product,
        status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
    
)
async def create_product(product:Product = Body(...)):
    new_product = await product_collection.insert_one(
        product.model_dump(by_alias=True,exclude =["id"])
    )
    created_product= await product_collection.find_one(
        {"_id":new_product.inserted_id}
    )
    return created_product


@app.get("/products/",
    response_description="List all products",
    response_model = ProductCollection,
    response_model_by_alias = False,
    
    )
async def list_products():
    ## this response is unpaginated ... TODO pagination
    return ProductCollection(products = await product_collection.find().to_list(1000))

@app.get("/order/",
         response_model = OrderCollection,
          response_model_by_alias = False)
async def list_order():
    return OrderCollection(order = await order_collection.find().to_list(100))
         
@app.post("/order/",
    response_model= Order,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False
)
async def create_order(order:Order = Body(...)):
     new_order = await order_collection.insert_one(
        order.model_dump(by_alias=True,exclude =["id"])
    )
     created_order= await order_collection.find_one(
        {"_id":new_order.inserted_id}
    )
     return created_order

