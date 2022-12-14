.PHONY: all build install typing lint test

all: black build install typing lint test

black:
	black -l 99 overlap_check tests
	isort --atomic .

build:
	python3 -m pip install --extra-index-url https://devstack.vwgroup.com/artifactory/api/pypi/pypi/simple -r requirements.txt

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .mypy_cache
	rm -fr .pytest_cache

install:
	python3 -m pip install -e .

typing:
	pytest -v -s --mypy overlap_check

lint:
	isort --check --diff overlap_check tests
	flake8 -v --statistics --count .
	black -l 99 --diff --check overlap_check tests

test:
	pytest -v -s --cov=overlap_check tests
	coverage html
