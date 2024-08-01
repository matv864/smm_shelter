deps:
	python -m pip install poetry

run:
	poetry install
	poetry run uvicorn src.app:app --reload --host 0.0.0.0 --port 8002

old_run:
	uvicorn src.app:app --reload --host 0.0.0.0 --port 8002