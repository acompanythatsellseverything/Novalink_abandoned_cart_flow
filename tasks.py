from celery import Celery
import time
from services.cart_service import NovalinkAbandonedCart

celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery.task
def process_abandoned_cart(email: str):
    NovalinkAbandonedCart().main(email)