from celery import Celery
import time
from services.cart_service import NovalinkAbandonedCart

celery = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery.task
def process_abandoned_cart_task(cart_data: dict):
    NovalinkAbandonedCart().main(cart_data)
