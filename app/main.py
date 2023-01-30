from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

# from infra.sqlalchemy.config.database import create_db

from .infra.sqlalchemy.routes import category, products

origins = ["http://localhost:4200"]


# create_db()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "API is running on port 8000"}


app.include_router(category.router)
app.include_router(products.router)
