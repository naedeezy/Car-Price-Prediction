from fastapi import FastAPI, Path
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

class CarInfo(BaseModel):
    brand: str
    milage: int
    accident: int
    clean_title: float
    interior_color: str
    exterior_color: str
    tsm: str
    fuel: str
    Engine_Displacement: float
    age: int

with open('pipe.pkl', 'rb') as f:
    model = pickle.load(f)

@app.post('/')
async def pricing_function(price:CarInfo):
    df = pd.DataFrame([price.dict().values()], columns=price.dict().keys())
    pred = model.predict(df)
    return {f'Your car would likely cost ${pred[0]}'}

