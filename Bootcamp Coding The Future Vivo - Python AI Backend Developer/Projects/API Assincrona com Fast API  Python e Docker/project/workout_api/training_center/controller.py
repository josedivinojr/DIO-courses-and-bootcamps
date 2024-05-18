from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select
from workout_api.generic.dependencies import DatabaseDependencies
from workout_api.training_center.schema import TrainingCenterIn, TrainingCenterOut
from workout_api.training_center.model import TrainingCenterModel

router = APIRouter()

@router.get(
        path='/',
        summary="Consult all training centers",
        status_code=status.HTTP_200_OK,
        response_model=list[TrainingCenterOut])
async def get_all(db_session: DatabaseDependencies) -> list[TrainingCenterOut]:

    training_centers: list[TrainingCenterOut] = (await db_session.execute(select(TrainingCenterModel))).scalars().all()
    return training_centers

@router.get(path='/{id}',summary="Consult training center",status_code=status.HTTP_200_OK, response_model=TrainingCenterOut)
async def get(id: UUID4, db_session: DatabaseDependencies) -> list[TrainingCenterOut]:
    training_center: TrainingCenterOut = (await db_session.execute(
        select(TrainingCenterModel).filter_by(id=id))).scalars().first()

    if not training_center:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'There is no training center of ID: {id}'
        )
    
    return training_center

@router.post(
        path='/',
        summary="Register a new training center",
        status_code=status.HTTP_201_CREATED)
async def post(
    db_session: DatabaseDependencies,
    training_center_in: TrainingCenterIn= Body(...)
    ) -> TrainingCenterOut:

    training_center_out = TrainingCenterOut(id=uuid4(), **training_center_in.model_dump())
    training_center_model = TrainingCenterModel(**training_center_out.model_dump())


    db_session.add(training_center_model)
    await db_session.commit()
    
    return training_center_out
