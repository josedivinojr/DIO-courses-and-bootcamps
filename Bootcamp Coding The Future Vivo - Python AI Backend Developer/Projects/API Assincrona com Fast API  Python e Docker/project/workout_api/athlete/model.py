from datetime import datetime
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.generic.models import BaseModel

class AtheleteModel(BaseModel):
    __tablename__ = "athlete"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[str] = mapped_column(String(11), nullable=False)
    height: Mapped[str] = mapped_column(String(11), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    # Category relationship
    category: Mapped['CategoryModel'] = relationship(back_populates='athlete')
    category_id = Mapped[int] = mapped_column(ForeignKey('category.pk_id'))

    # TrainingCenter relationship
    category: Mapped['TrainingCenter'] = relationship(back_populates='athlete')
    category_id = Mapped[int] = mapped_column(ForeignKey('trainingcenter.pk_id'))
