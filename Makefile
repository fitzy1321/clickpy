run:
	python -m clickpy

test:
	poetry run pytest tests/ --cov=clickpy -v

coverage:
	poetry run coverage html && open htmlcov/index.html

# VERSION = $(shell $(poetry version -s))
# tag: $(VERSION)
# 	git tag $?
