import os
from typing import Optional, List
from datetime import datetime
from typing import Annotated
from fastapi import FastAPI, Body, HTTPException, status

from pydantic import ConfigDict, BaseModel, Field, EmailStr
from pydantic import BaseModel, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Product(BaseModel):
    id: Optional[PyObjectId] = Field(alias = "_id",default = None)
    name: str  = Field(...)
    price: float = Field(gt = 0)
    available_quantity : int =Field(default = 0)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "Ink",
                "price": 3.0,
                "available_quantity": 34,
                
            }
        },
    )
class ProductCollection(BaseModel):
    products:List[Product]
# class Order(BaseModel):
#     name:str

class Address(BaseModel):
    City:str
    Country:str
    zipcode:int

class OrderedItem(BaseModel):
    productId :str
    quantity:int


class Order(BaseModel):
    id: Optional[PyObjectId] = Field(alias = "_id",default = None)
    createdOn :datetime = datetime.now()
    items :list[OrderedItem] = Field(...)
    total_amount : float
    address :Address
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "items": [{"productId":"roiasntsn","quantity":3},{"productId":"roiasntsn","quantity":3}],
                "total_amount": 34.4,
                "address": {"City":"rastra",
                            "Country":"ratrast",
                            "zipcode":234343},
                
            }
        },
    )

class OrderCollection(BaseModel):
    order:list[Order]