install:
	poetry install

build:
	poerty build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

diff:
	poetry run gendiff fixtures/file1.json fixtures/file2.json