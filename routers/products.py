
from fastapi import APIRouter, HTTPException
from models import Product
from typing import List

router = APIRouter(prefix="/products", tags=["products"])

products_db = []

@router.get("/", response_model=List[Product])
def get_products():
    return products_db

@router.post("/", response_model=Product)
def create_product(product: Product):
    product_dict = product.dict()
    product_dict["id"] = len(products_db) + 1
    products_db.append(product_dict)
    return product_dict

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products_db:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
