from typing import List
from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from src.models.product import ProductModel
from src.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from src.database.mongo import db_client
from src.core.exceptions import NotFoundException

import pymongo


class ProductUseCase:
    """
    Use case class for managing product operations in the database.
    """

    def __init__(self) -> None:
        """
        Initializes the ProductUseCase with a MongoDB client, database, and collection.
        """
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        """
        Creates a new product in the database.

        Args:
            body (ProductIn): The product data to create.

        Returns:
            ProductOut: The created product data.
        """
        product_model = ProductModel(**body.model_dump())
        await self.collection.insert_one(product_model.model_dump())

        product = ProductOut(**product_model.model_dump())

        return product

    async def get(self, id: UUID) -> ProductOut:
        """
        Retrieves a product from the database by its ID.

        Args:
            id (UUID): The ID of the product to retrieve.

        Returns:
            ProductOut: The retrieved product data.

        Raises:
            NotFoundException: If the product with the given ID is not found.
        """
        result = await self.collection.find_one({"id": id})

        if not result:
            raise NotFoundException(message=f"Product Not Found with id: {id}")
        return ProductOut(**result)

    async def query(self) -> List[ProductOut]:
        """
        Retrieves all products from the database.

        Returns:
            List[ProductOut]: A list of all products.
        """
        return [ProductOut(**item) async for item in self.collection.find()]

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        """
        Updates a product in the database by its ID.

        Args:
            id (UUID): The ID of the product to update.
            body (ProductUpdate): The updated product data.

        Returns:
            ProductUpdateOut: The updated product data.
        """
        product = ProductUpdate(**body.model_dump(exclude_none=True))
        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": product.model_dump(exclude_none=True)},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        return ProductUpdateOut(**result)

    async def delete(self, id: UUID) -> bool:
        """
        Deletes a product from the database by its ID.

        Args:
            id (UUID): The ID of the product to delete.

        Returns:
            bool: True if the product was successfully deleted, False otherwise.

        Raises:
            NotFoundException: If the product with the given ID is not found.
        """
        product = await self.collection.find_one({"id": id})

        if not product:
            raise NotFoundException(message=f"Product Not Found with id: {id}")

        result = await self.collection.delete_one({"id": id})

        return True if result.deleted_count > 0 else False


product_usecase = ProductUseCase()
