from typing import Annotated
from pydantic import Field, UUID4
from workout_api.generic.schemas import BaseSchema

class TrainingCenterIn(BaseSchema):
    name: Annotated[str, Field(description='Training Center Name', example='BodyTech', max_length=20)]
    address: Annotated[str, Field(description='Training Center Address', example='Rua do Pinho', max_length=60)]
    owner: Annotated[str, Field(description='Training Center Owner', example='Ribeiro', max_length=30)]

class TrainingCenter(BaseSchema):
    name: Annotated[str, Field(description='Training Center Name', example='BodyTech', max_length=20)]

class TrainingCenterOut(TrainingCenterIn):
    id: Annotated[UUID4, Field(description='Training Center Identifier')]    