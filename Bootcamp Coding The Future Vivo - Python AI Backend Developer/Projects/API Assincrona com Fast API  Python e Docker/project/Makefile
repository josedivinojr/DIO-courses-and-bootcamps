run:
	@ uvicorn workout_api.main:app --reload

create-migrations:
	@PYTHONPATH=PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(description)

run-migrations:
	@PYTHONPATH=PYTHONPATH:$(pwd) alembic upgrade head