.PHONY: setup test build check_version publish clean

setup:
	pip install flit
	flit install -s

test:
	pytest

build:
	flit build

MODULE_VERSION := $(shell python -c "from dotenv_stripout import __version__ as v; print(v)" | tail -n1)

check_version:
	[ "refs/tags/${MODULE_VERSION}" = "${GITHUB_REF}" ]

publish: check_version build
	flit publish

clean:
	isort ./**/*.py
	black . --line-length 80
	flake8 . --max-line-length 80 --ignore=E501,W291
	rm -rf dist **/dist
	rm -rf *.pyc **/*.pyc
	rm -rf .hypothesis **/.hypothesis
	rm -rf .pytest_cache **/.pytest_cache
	rm -rf __pycache__ ./**/__pycache__
