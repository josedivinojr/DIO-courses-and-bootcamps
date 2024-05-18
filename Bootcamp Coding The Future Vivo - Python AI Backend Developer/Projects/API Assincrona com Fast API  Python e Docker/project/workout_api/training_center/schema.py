from typing import Annotated
from pydantic import Field, PositiveFloat
from workout_api.generic.schemas import BaseSchema

class TrainingCenter(BaseSchema):
    name: Annotated[str, Field(description='Training Center Name', example='BodyTech', max_length=20)]
    address: Annotated[str, Field(description='Training Center Address', example='Rua do Pinho', max_length=60)]
    owner: Annotated[str, Field(description='Training Center Owner', example='Ribeiro', max_length=30)]

