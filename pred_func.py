import pandas as pd
from fastapi import FastAPI
from sklearn.neighbors import KNeighborsClassifier
import pickle
from pydantic import BaseModel
import uvicorn

model: KNeighborsClassifier = pickle.load(open("model.pkl", "rb"))


class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


app = FastAPI()


@app.get("/pred")
def pred():
    return {"msg": "hello"}
    # return data.model_dump()
    data = data.model_dump()
    data = pd.DataFrame(data, index=[0])
    data.columns = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
    ]
    print(data)
    pred = model.predict(data)
    pred = pred.squeeze().tolist()
    return {"msg": "hello", "prediction": pred}


if __name__ == "__main__":
    uvicorn.run("pred_func:app", host="0.0.0.0", port=8080)
