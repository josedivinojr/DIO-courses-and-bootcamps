from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.generic.models import BaseModel

class CategoryModel(BaseModel):
    __tablename__ = "category"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    athlete: Mapped['AthleteModel'] = relationship(back_populates='category')
