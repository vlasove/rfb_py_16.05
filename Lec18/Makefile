.PHONY: format, lint, check

format:
	black example_c.py && docformatter -i example_c.py && isort example_c.py

lint:
	pylint example_c.py

check:
	mypy example_c.py

.DEFAULT_GOAL := format