from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ..config.database import get_db

from ..schemas.schemas import Category
from ..repository.category import CategoryRepository

router = APIRouter()


@router.get("/category", status_code=status.HTTP_200_OK)
def get_all_category(db: Session = Depends(get_db)):
    category = CategoryRepository(db).get_all()
    return category


@router.get("/category/{id}", status_code=status.HTTP_200_OK)
def get_category_by_pk(
    id: int, response: Response, db: Session = Depends(get_db)
):
    category = CategoryRepository(db).get_by_pk(id)
    if category:
        return category
    response.status_code = status.HTTP_404_NOT_FOUND


@router.post("/category", status_code=status.HTTP_201_CREATED)
def add_category(category: Category, db: Session = Depends(get_db)):
    new_category = CategoryRepository(db).create(category)
    return new_category


@router.put("/category/{category_id}", status_code=status.HTTP_200_OK)
def update_category(
    category_id: int,
    response: Response,
    new_category: Category,
    db: Session = Depends(get_db),
):
    old_category: Category = CategoryRepository(db).get_by_pk(category_id)
    if old_category:
        CategoryRepository(db).update_by_pk(old_category, new_category)
        return {"message": "Category updated successfully"}
    response.status_code = status.HTTP_404_NOT_FOUND


@router.delete("/category/{category_id}", status_code=status.HTTP_202_ACCEPTED)
def delete_category(
    category_id: int, response: Response, db: Session = Depends(get_db)
):
    category: Category = CategoryRepository(db).get_by_pk(category_id)
    if category:
        CategoryRepository(db).destroy(category_id)
        return {"message": "Category deleted"}
    response.status_code = status.HTTP_404_NOT_FOUND
