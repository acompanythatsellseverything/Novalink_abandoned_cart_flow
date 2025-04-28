from fastapi import FastAPI
from pydantic import BaseModel
from tasks import process_abandoned_cart
from services.cart_service import NovalinkAbandonedCart
from typing import List, Optional
import uvicorn

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
    # wait 20 min
    # process_abandoned_cart.apply_async((email,), countdown=2)#20*60
    # print(data)
    NovalinkAbandonedCart().main(data)
    

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

    