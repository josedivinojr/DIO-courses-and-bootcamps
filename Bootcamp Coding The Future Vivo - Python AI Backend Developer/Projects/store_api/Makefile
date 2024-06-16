# run FastAPI app
run:
	@uvicorn src.main:app --reload

# run Pytest tests :D
test:
	@python3.12 -m pytest

match-test:
	@python3.12 -m pytest -s -rx -k $(K) --pdb src ./tests/
