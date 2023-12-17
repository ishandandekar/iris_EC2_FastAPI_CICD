import json
import os
from uuid import uuid4
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mangum import Mangum


class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


app = FastAPI()
handler = Mangum(app)


@app.get("/")
async def root():
    return {"message": "Welcome to my API"}


@app.get("/pred")
def pred():
    return {"msg": "hello"}
