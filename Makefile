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
	poetry run pytest -v -vv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

diff:
	poetry run gendiff tests/fixtures/nested1.yml tests/fixtures/nested2.yml --format=json

diff_plain:
	poetry run gendiff tests/fixtures/plain1.json tests/fixtures/plain2.json