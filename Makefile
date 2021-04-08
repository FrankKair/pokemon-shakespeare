.PHONY: all test clean

test:
	pytest -vv src

dev:
	PYTHON_ENV=development uvicorn main:app --port=5000 --reload

build:
	docker build -t pokemon-shakespeare .

run:
	docker run --name pkm-shakespeare-container -e PORT=5000 -p 5000:5000 -it --rm pokemon-shakespeare

