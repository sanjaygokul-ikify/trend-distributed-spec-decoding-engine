build: poetry build

develop: poesy install -e

test: python -m pytest tests

lint: flake8 src

deploy: poetry publish

clean: find . -type d -name '__pycache__' -exec rm -rf {} +