
from typing import Annotated
from pydantic import Field
from workout_api.generic.schemas import BaseSchema


class Category(BaseSchema):
        name: Annotated[str, Field(description='Category Name', example='Bodybuild', max_length=10)]
