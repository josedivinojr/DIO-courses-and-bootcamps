from fastapi import FastAPI
from workout_api.router import router

app = FastAPI(title="Workout API")

app.include_router(router)
