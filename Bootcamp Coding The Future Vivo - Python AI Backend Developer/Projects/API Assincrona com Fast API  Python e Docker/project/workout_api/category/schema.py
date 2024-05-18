
from typing import Annotated
from pydantic import Field, UUID4
from workout_api.generic.schemas import BaseSchema

class CategoryIn(BaseSchema):
	name: Annotated[str, Field(description='Category Name', example='Bodybuild', max_length=10)]

class CategoryOut(CategoryIn):
    id: Annotated[UUID4, Field(description="Category Identifier")]
