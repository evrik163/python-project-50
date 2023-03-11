install:
	poetry install

package-install:
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

reinstall:
	pip install --user --force-reinstall dist/*.whl

publish:
	poetry publish --dry-run

push:
	git push --set-upstream origin main

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test_coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/
