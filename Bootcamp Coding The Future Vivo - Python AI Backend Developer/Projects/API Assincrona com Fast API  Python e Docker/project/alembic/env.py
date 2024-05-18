"""
This script provides functions to manage database migrations using Alembic.
It supports both offline and online migration execution.

**Imports:**

* `asyncio`: For asynchronous operations (online migrations).
* `logging.config.fileConfig`: For configuring logging from a file.
* `sqlalchemy.engine.Connection`: Represents a connection to the database.
* `sqlalchemy.ext.asyncio.async_engine_from_config`: Creates an asynchronous SQLAlchemy engine from configuration.
* `sqlalchemy.pool`: Provides connection pooling mechanisms.
* `alembic.context`: Provides access to the Alembic configuration object.
* `workout_api.contrib.models.BaseModel`: Base class for models in the `workout_api` application (likely).
* `workout_api.contrib.repository.models`: All models from the `workout_api.contrib.repository` module (likely).

**Global Variable:**

* `target_metadata`: SQLAlchemy MetaData object representing the database schema for migrations.

**Functions:**

* `run_migrations_offline()`: Executes migrations in offline mode (without a database connection).
* `do_run_migrations(connection: Connection)`: Performs the actual migration execution using the provided connection.
* `run_async_migrations()`: Executes migrations in online mode (asynchronously with a database connection).
* `run_migrations_online()`: Runs the `run_async_migrations` function using `asyncio.run`.
"""

import asyncio
from logging.config import fileConfig

from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy import pool

from alembic import context
from workout_api.generic.models import BaseModel
from workout_api.generic.repository.models import AtheleteModel, CategoryModel, TrainingCenterModel

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = BaseModel.metadata


def run_migrations_offline() -> None:
    """
    Executes migrations in offline mode (without a database connection).

    This function retrieves the database URL from the Alembic configuration 
    and configures the Alembic context with that URL, target metadata, 
    literal binds, and specific dialect options. It then runs the migrations 
    within a transaction using the Alembic context.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None: 
    """
    Performs the actual migration execution using the provided connection.

    This function configures the Alembic context with the provided connection 
    and target metadata. It then runs the migrations within a transaction 
    using the Alembic context.
    """
    context.configure(connection=connection, target_metadata=target_metadata)
    
    with context.begin_transaction():
        context.run_migrations()

async def run_async_migrations() -> None:
    """
    Executes migrations in online mode (asynchronously with a database connection).

    This function creates an asynchronous SQLAlchemy engine from the Alembic 
    configuration and connects to it asynchronously. It then runs the 
    `do_run_migrations` function within the connection using `connection.run_sync`.
    """
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


def run_migrations_online() -> None:
    """
    Runs the `run_async_migrations` function using `asyncio.run`.

    This function simply calls `asyncio.run` to execute the `run_async_migrations` 
    function asynchronously.
    """
    asyncio.run(run_async_migrations())

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()