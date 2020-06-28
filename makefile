.PYHONY: test
test:
	FLASK_ENV=testing pytest -vv

.PYHONY: cov
cov:
	FLASK_ENV=testing pytest -vv --cov=app/ && coveralls

.PYHONY: update-test
update-test:
	FLASK_ENV=testing @pytest --force-regen

.PYHONY: check
check:
	@black . --check --exclude=".venv"

.PYHONY: format
format:
	@black . --exclude=".venv"

