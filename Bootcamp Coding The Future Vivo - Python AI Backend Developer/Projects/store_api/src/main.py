from fastapi import FastAPI

from src.core.settings import settings
from src.routers import api_router


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            version="0.0.1",
            title=settings.PROJECT_NAME,
            root_path=settings.ROOT_PATH
        )


app = App()
app.include_router(api_router)