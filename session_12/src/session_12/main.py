from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
import os

api = FastAPI(
    title="TODO Etic_Algarve API")

DB_USER = os.getenv("DB_USER", None)
DB_PASS = os.getenv("DB_PASS", None)
DB_HOST = os.getenv("DB_HOST", None)
DB_PORT = os.getenv("DB_PORT", None)
DB_NAME = os.getenv("DB_NAME", None)

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

SQLModel.metadata.create_all(engine)

@api.post("/task")
def create_task():
    pass

@api.get("/task")
def list_task():
    pass

@api.put("/task")
def edit_task():
    pass

@api.patch("/task")
def close_task():
    pass

@api.delete("/task")
def delete_task():
    pass