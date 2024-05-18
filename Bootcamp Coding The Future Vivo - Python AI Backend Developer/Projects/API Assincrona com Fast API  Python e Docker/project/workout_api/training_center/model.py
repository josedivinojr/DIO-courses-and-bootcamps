from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.generic.models import BaseModel

class TrainingCenter(BaseModel):
    __tablename__ = "trainingcenter"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    address: Mapped[str] = mapped_column(String(60), nullable=False)
    owner: Mapped[str] = mapped_column(String(30), nullable=False)
    athlete: Mapped['AthleteModel'] = relationship(backpopulates='athlete')
