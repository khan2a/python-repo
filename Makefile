install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	python -m pytest -vv -ra --cov=tests tests/

one-test:
	python -m pytest -vv tests/test_greeting.py::test_your_name

format:
	black *.py

lint:
	pylint --disable=R,C *.py

all: install lint test one-test format