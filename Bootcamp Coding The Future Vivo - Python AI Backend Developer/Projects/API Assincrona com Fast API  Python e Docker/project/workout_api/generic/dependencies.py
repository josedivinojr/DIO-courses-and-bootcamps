from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from workout_api.settings.database import get_session

DatabaseDependencies = Annotated[AsyncSession, Depends(get_session)]
