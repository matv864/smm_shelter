deps:
	python -m pip install poetry
	poetry install

old_deps:
	pip install -r requirements.txt

run:
	poetry run uvicorn src.app:app --reload --host 0.0.0.0 --port 8000

old_run:
	uvicorn src.app:app --reload --host 0.0.0.0 --port 8000