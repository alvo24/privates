.PHONY: setup run test lint

setup:
	python -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

run:
	. .venv/bin/activate && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

test:
	. .venv/bin/activate && pytest -q
