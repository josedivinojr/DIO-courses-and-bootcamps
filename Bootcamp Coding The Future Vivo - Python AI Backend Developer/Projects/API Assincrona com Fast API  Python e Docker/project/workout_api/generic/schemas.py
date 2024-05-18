from datetime import datetime
from typing import Annotated
from pydantic import UUID4, BaseModel, Field

class BaseSchema(BaseModel):
    class config:
        extra = 'forbid'
        from_attributes = True

class BaseSchemaOut(BaseModel):
    id: Annotated[UUID4, Field(description="Identifier")]
    created_at: Annotated[datetime, Field(description="Created Time")]
