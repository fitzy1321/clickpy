run:
	poetry run python -m clickpy

test:
	poetry run pytest tests/ --cov=clickpy -v --capture=tee-sys

coverage:
	poetry run coverage html && open htmlcov/index.html

check:
	flake8 .

# VERSION = $(shell $(poetry version -s))
# tag: $(VERSION)
# 	git tag $?
