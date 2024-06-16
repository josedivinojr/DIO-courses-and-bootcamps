from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from pydantic import UUID4
from src.core.exceptions import NotFoundException

from src.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from src.usecases.product import ProductUseCase

router = APIRouter(tags=["products"])


@router.post(path="/", status_code=status.HTTP_201_CREATED)
async def post(
    body: ProductIn = Body(...), usecase: ProductUseCase = Depends()
) -> ProductOut:
    """
    Create a new product.

    Args:
        body (ProductIn): The product data to create.
        usecase (ProductUseCase): The use case instance to handle the product creation.

    Returns:
        ProductOut: The created product.
    """
    return await usecase.create(body=body)


@router.get(path="/{id}", status_code=status.HTTP_200_OK)
async def get(
    id: UUID4 = Path(alias="id"), usecase: ProductUseCase = Depends()
) -> ProductOut:
    """
    Retrieve a product by its ID.

    Args:
        id (UUID4): The unique identifier of the product.
        usecase (ProductUseCase): The use case instance to handle the product retrieval.

    Returns:
        ProductOut: The retrieved product.

    Raises:
        HTTPException: If the product is not found.
    """
    try:
        return await usecase.get(id=id)
    except NotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.get(path="/", status_code=status.HTTP_200_OK)
async def query(usecase: ProductUseCase = Depends()) -> List[ProductOut]:
    """
    Retrieve a list of all products.

    Args:
        usecase (ProductUseCase): The use case instance to handle the product query.

    Returns:
        List[ProductOut]: A list of all products.
    """
    return await usecase.query()


@router.patch(path="/{id}", status_code=status.HTTP_200_OK)
async def patch(
    id: UUID4 = Path(alias="id"),
    body: ProductUpdate = Body(...),
    usecase: ProductUseCase = Depends(),
) -> ProductUpdateOut:
    """
    Update an existing product by its ID.

    Args:
        id (UUID4): The unique identifier of the product.
        body (ProductUpdate): The updated product data.
        usecase (ProductUseCase): The use case instance to handle the product update.

    Returns:
        ProductUpdateOut: The updated product.
    """
    return await usecase.update(id=id, body=body)


@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    id: UUID4 = Path(alias="id"), usecase: ProductUseCase = Depends()
) -> None:
    """
    Delete a product by its ID.

    Args:
        id (UUID4): The unique identifier of the product.
        usecase (ProductUseCase): The use case instance to handle the product deletion.

    Raises:
        HTTPException: If the product is not found.
    """
    try:
        await usecase.delete(id=id)
    except NotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
