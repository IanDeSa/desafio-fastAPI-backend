from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from infra.sqlalchemy.config.database import get_db

from infra.sqlalchemy.schemas.schemas import Product
from infra.sqlalchemy.repository.product import ProductRepository

router = APIRouter()


@router.get("/products", status_code=status.HTTP_200_OK)
def get_all_products(db: Session = Depends(get_db)):
    products = ProductRepository(db).get_all()
    return products


@router.get("/products/{id}", status_code=status.HTTP_200_OK)
def get_by_pk(id: int, response: Response, db: Session = Depends(get_db)):
    products = ProductRepository(db).get_by_pk(id)
    if products:
        return products
    response.status_code = status.HTTP_404_NOT_FOUND


@router.post("/products", status_code=status.HTTP_201_CREATED)
def add_product(product: Product, db: Session = Depends(get_db)):
    new_product = ProductRepository(db).create(product)
    return new_product


@router.put("/products/{product_id}", status_code=status.HTTP_200_OK)
def update_product(
    product_id: int,
    response: Response,
    new_product: Product,
    db: Session = Depends(get_db),
):
    old_product: Product = ProductRepository(db).get_by_pk(product_id)
    if old_product:
        ProductRepository(db).update_by_pk(old_product, new_product)
        return {"message": "Product updated successfully"}
    response.status_code = status.HTTP_404_NOT_FOUND


@router.delete("/products/{product_id}", status_code=status.HTTP_202_ACCEPTED)
def delete_product(
    product_id: int, response: Response, db: Session = Depends(get_db)
):
    product: Product = ProductRepository(db).get_by_pk(product_id)
    if product:
        ProductRepository(db).destroy(product_id)
        return {"message": "Product deleted"}
    response.status_code = status.HTTP_404_NOT_FOUND
