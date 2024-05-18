from fastapi import APIRouter
from workout_api.athlete.controller import router as athlete
from workout_api.category.controller import router as category
from workout_api.training_center.controller import router as training_center


router = APIRouter()
router.include_router(athlete, prefix='/athletes', tags=['athletes'])
router.include_router(category, prefix='/category', tags=['category'])
router.include_router(training_center, prefix='/training_center', tags=['training_center'])
