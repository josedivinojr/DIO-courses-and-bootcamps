from fastapi import APIRouter, status, Body

from workout_api.generic.dependencies import DatabaseDependencies
from workout_api.athlete.schema import AthleteIn

router = APIRouter()

@router.post(path='/',
        summary="Register a new athlete",
        status_code=status.HTTP_201_CREATED)
async def post(
    db_session: DatabaseDependencies,
    athlete_in: AthleteIn = Body(...) ):
    pass
