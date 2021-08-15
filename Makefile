.PHONY: setup lint check_version build publish clean

# commands for building the package
setup:
	pip install flit
	flit install -s

lint:
	isort *.py
	black --line-length 80
	flake8 --ignore=E501,W291

build: clean lint
	flit build

MODULE_VERSION := $(shell python -c "from dotenv_stripout import __version__ as v; print(v)" | tail -n1)

check_version:
	[ "refs/tags/${MODULE_VERSION}" = "${GITHUB_REF}" ]

publish: check_version build
	flit publish

# general commands
clean:
	isort
	black . --line-length 80
	flake8 . --max-line-length 80
	rm -rf *.pyc **/*.pyc
	rm -rf .hypothesis **/.hypothesis
	rm -rf .pytest_cache **/.pytest_cache
	rm -rf __pycache__ ./**/__pycache__
