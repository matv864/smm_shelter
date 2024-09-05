deps:
	python -m pip install poetry
	poetry install

run:
	poetry run uvicorn src.app:app --host 0.0.0.0 --forwarded-allow-ips='*' --proxy-headers
