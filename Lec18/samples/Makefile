.PHONY: format, lint, check, test

format:
	black example_b.py && docformatter -i example_b.py && isort example_b.py

lint:
	pylint example_b.py

check:
	mypy example_b.py

test:
	python -m unittest test_example_b.py

.DEFAULT_GOAL := format