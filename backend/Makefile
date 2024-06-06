deps:
	python -m pip install poetry
	poetry install

run:
	poetry run uvicorn src.app:app --reload --host 0.0.0.0 --port 8002

old_run:
	uvicorn src.app:app --reload --host 0.0.0.0 --port 8002