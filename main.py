from fastapi import FastAPI
from pydantic import BaseModel
from tasks import process_abandoned_cart_task
from services.cart_service import NovalinkAbandonedCart
from typing import List, Optional
import uvicorn
from fastapi.encoders import jsonable_encoder


app = FastAPI()

class SimType(BaseModel):
    simType: str
    brand: Optional[str] = None
    model: Optional[str] = None

class PlanData(BaseModel):
    id: int
    plan: str
    data: str
    timeline: str
    simType: SimType
    price: float
    quantity: int
    plan_soc: str
    priceId: str

class CartData(BaseModel):
    email: str
    user_id: int
    plans: List[PlanData]

@app.post("/")
async def cart_data(data: CartData):
    data_dict = jsonable_encoder(data)
    process_abandoned_cart_task.apply_async((data_dict,), countdown=20*60)
    return {"status": "scheduled"}
    

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

    