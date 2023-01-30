from sqlalchemy.orm import Session
from ..schemas import schemas
from ..models import models
from sqlalchemy import delete


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: schemas.Product):
        db_product: schemas.Product = models.Product(
            id=product.id,
            name=product.name,
            category_id=product.category_id,
            price=product.price,
            serie=product.serie,
        )
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get_all(self):
        products = self.db.query(models.Product).all()
        return products

    def get_by_pk(self, id: int):
        products = self.db.get(models.Product, id)
        return products

    def update_by_pk(
        self, old_product: schemas.Product, new_product: schemas.Product
    ):
        self.db.query(models.Product).filter(
            models.Product.name == old_product.name
        ).update({"name": new_product.name})
        self.db.query(models.Product).filter(
            models.Product.category_id == old_product.category_id
        ).update({"category_id": new_product.category_id})
        self.db.query(models.Product).filter(
            models.Product.price == old_product.price
        ).update({"price": new_product.price})
        self.db.query(models.Product).filter(
            models.Product.serie == old_product.serie
        ).update({"serie": new_product.serie})
        self.db.commit()

    def destroy(self, product_id: int):
        stmt = delete(models.Product).where(models.Product.id == product_id)
        self.db.execute(stmt)
        self.db.commit()
