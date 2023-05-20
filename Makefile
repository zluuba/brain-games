install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

reinstall:
	python3 -m pip install --force-reinstal --user dist/*.whl

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 brain_games

test:
	poetry run pytest brain_games

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
