from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select
from workout_api.generic.dependencies import DatabaseDependencies
from workout_api.category.schema import CategoryIn, CategoryOut
from workout_api.category.model import CategoryModel

router = APIRouter()

@router.get(
        path='/',
        summary="Consult all categories",
        status_code=status.HTTP_200_OK,
        response_model=list[CategoryOut])
async def get_all(db_session: DatabaseDependencies) -> list[CategoryOut]:

    categories: list[CategoryOut] = (await db_session.execute(select(CategoryModel))).scalars().all()
    return categories

@router.get(
        path='/{id}',
        summary="Consult category",
        status_code=status.HTTP_200_OK,
        response_model=CategoryOut)
async def get(id: UUID4, db_session: DatabaseDependencies) -> list[CategoryOut]:
    category: CategoryOut = (await db_session.execute(
        select(CategoryModel).filter_by(id=id))).scalars().first()

    if not category:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'There is no category of ID: {id}'
        )
    
    return category


@router.post(
        path='/',
        summary="Register a new category",
        status_code=status.HTTP_201_CREATED)
async def post(
    db_session: DatabaseDependencies,
    category_in: CategoryIn= Body(...)
    ) -> CategoryOut:

    category_out = CategoryOut(id=uuid4(), **category_in.model_dump())
    category_model = CategoryModel(**category_out.model_dump())


    db_session.add(category_model)
    await db_session.commit()
    
    return category_out
