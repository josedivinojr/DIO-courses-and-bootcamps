from typing import Annotated
from pydantic import Field, PositiveFloat
from workout_api.generic.schemas import BaseSchema
from workout_api.generic.schemas import BaseSchemaOut

class Athlete(BaseSchema):
    name: Annotated[str, Field(description='Athlete Name', example='Matias', max_length=50)]
    cpf: Annotated[str, Field(description='Athlete CPF', example='13087536784', max_length=11)]
    age: Annotated[int, Field(description='Athlete Age', example=26)]
    weight: Annotated[PositiveFloat, Field(description='Athlete Weight', example=80.7)]
    height: Annotated[PositiveFloat, Field(description='Athlete Height', example=1.76)]
    sex: Annotated[str, Field(description='Athlete Sext', example='M', max_length=1)]

class AthleteIn(Athlete):
    pass
class AthleteOut(Athlete, BaseSchemaOut):
    name: Annotated[str, Field(description='Athlete Name', example='Matias', max_length=50)]
    cpf: Annotated[str, Field(description='Athlete CPF', example='13087536784', max_length=11)]
    age: Annotated[int, Field(description='Athlete Age', example=26)]
    weight: Annotated[PositiveFloat, Field(description='Athlete Weight', example=80.7)]
    height: Annotated[PositiveFloat, Field(description='Athlete Height', example=1.76)]
    sex: Annotated[str, Field(description='Athlete Sext', example='M', max_length=1)]
