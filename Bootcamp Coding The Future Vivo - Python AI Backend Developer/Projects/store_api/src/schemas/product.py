from decimal import Decimal
from typing import Annotated, Optional
from bson import Decimal128
from pydantic import AfterValidator, Field
from src.schemas.base import BaseSchemaMixin, OutMixin


class ProductBase(BaseSchemaMixin):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: Decimal = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn, OutMixin):
    ...


def convert_decimal_128(value):
    return Decimal128(str(value))


_Decimal = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductUpdate(BaseSchemaMixin):
    # only allows to update these fields

    quantity: Optional[int] = Field(None, description="Product quantity")
    price: Optional[_Decimal] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")

    ...


class ProductUpdateOut(ProductOut):
    ...
