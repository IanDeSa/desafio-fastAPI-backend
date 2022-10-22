from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    id: Optional[int] = None
    name: str
    category_id: int
    price: float
    serie: int

    class Config:
        orm_mode: True


class Category(BaseModel):
    id: Optional[int] = None
    name: str

    class Config:
        orm_mode: True


class ProductCategory(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    serie: int
    category: str

    class Config:
        orm_mode: True
