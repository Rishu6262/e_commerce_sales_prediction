from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pickle
import numpy as np
import os

BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "sales_model.pkl")

model = pickle.load(open(model_path, "rb"))

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# mappings based on your dataset
product_map = {
    "Printer": 0,
    "Mouse": 1,
    "Tablet": 2,
    "Camera": 3,
    "Headphones": 4,
    "Smartwatch": 5,
    "Monitor": 6,
    "Smartphone": 7,
    "Keyboard": 8,
    "Laptop": 9
}

category_map = {
    "Office": 0,
    "Accessories": 1,
    "Electronics": 2
}

region_map = {
    "North": 0,
    "East": 1,
    "South": 2,
    "West": 3
}


class SalesInput(BaseModel):
    product_name: str
    category: str
    region: str
    quantity: int
    year: int
    month: int
    day: int


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/predict")
def predict(data: SalesInput):
    features = np.array([[
        product_map[data.product_name],
        category_map[data.category],
        region_map[data.region],
        data.quantity,
        data.year,
        data.month,
        data.day
    ]])

    prediction = model.predict(features)

    return {
        "predicted_sales": float(prediction[0])
    }