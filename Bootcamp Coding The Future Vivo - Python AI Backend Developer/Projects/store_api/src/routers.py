from fastapi import APIRouter
from src.controllers.product import router as product

api_router = APIRouter()
api_router.include_router(product, prefix="/products")
