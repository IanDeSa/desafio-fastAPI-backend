from fastapi import FastAPI

from infra.sqlalchemy.config.database import create_db

from infra.sqlalchemy.routes import category
from infra.sqlalchemy.routes import products


create_db()


app = FastAPI()


@app.get("/")
def home():
    return {"message": "API is running on port 8000"}


app.include_router(category.router)
app.include_router(products.router)
