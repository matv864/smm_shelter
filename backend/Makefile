deps:
	pip install uv
	uv pip install --no-cache --system -r requirements.lock

run:
	fastapi run src/app.py --host 0.0.0.0 --reload
