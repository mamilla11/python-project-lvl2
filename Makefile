install:
	poetry install

build:
	poetry build

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
	poetry run gendiff tests/fixtures/before_nested.yml tests/fixtures/after_nested.yml

diff_plain:
	poetry run gendiff tests/fixtures/before_plain.json tests/fixtures/after_plain.json