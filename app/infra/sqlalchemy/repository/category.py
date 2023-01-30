from sqlalchemy.orm import Session
from ..schemas import schemas
from ..models import models
from sqlalchemy import delete


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, category: schemas.Category):
        db_category: schemas.Category = models.Category(
            id=category.id,
            name=category.name,
        )
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def get_all(self):
        category = self.db.query(models.Category).all()
        return category

    def get_by_pk(self, id: int):
        category = self.db.get(models.Category, id)
        return category

    def update_by_pk(
        self, old_category: schemas.Category, new_category: schemas.Category
    ):
        self.db.query(models.Category).filter(
            models.Category.name == old_category.name
        ).update({"name": new_category.name})
        self.db.commit()

    def destroy(self, category_id: int):
        stmt = delete(models.Category).where(models.Category.id == category_id)
        self.db.execute(stmt)
        self.db.commit()
