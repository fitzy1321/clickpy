run:
	poetry run python -m clickpy

test:
	poetry run pytest --capture=tee-sys tests/ --cov=clickpy -v

coverage:
	poetry run coverage html && open htmlcov/index.html

check:
	flake8 .

# VERSION = $(shell $(poetry version -s))
# tag: $(VERSION)
# 	git tag $?
